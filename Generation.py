from openai import OpenAI
import random
import time
import os
import pandas as pd
from docx import Document
from PromptsDict import prompt_templates  # Load the prompt dictionary

# === CONFIGURATION ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = 'gpt-4-turbo'
EXCEL_PATH = 'Book1.xlsx'
CHUNK_SIZE = 5

# === UTILITIES ===
def pick_random_topics(num=5, excel_path=EXCEL_PATH):
    try:
        df = pd.read_excel(excel_path)
        topic_column = df.columns[0]
        topics = df[topic_column].dropna().tolist()
        if len(topics) < num:
            raise ValueError(f"Only {len(topics)} topics available, but {num} requested.")
        return random.sample(topics, num)
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def format_topics(topics_list):
    return "\n".join([f"{i+1}. {topic}" for i, topic in enumerate(topics_list)]) 

def build_prompt_from_template(topics_list, template_key):
    topics_str = format_topics(topics_list)
    randomized_answer_key = ', '.join(str(n) for n in random.choices(range(1, 5), k=5))
    template = prompt_templates.get(template_key, "")
    return template.format(topics=topics_str, answer_key=randomized_answer_key)

def verify_prompt(questions_text):
    return f"""
im gonna send you 5 questions at once
you have to check whether or not they are correct
question, answer key, solution etc all should be 100% correct, if there is even a tiny fault or discrepancy, tell me
be very precise and unbiased, check very carefully
you dont need to repeat the questions and answers
just thoroughly check them if they are written correctly and then tell me for each question if it is correct or not, free of discrepancies or not. Are the answer keys correct? Are the solutions logical? Are any options misleading or repeated?
if there are any issues, tell me what and where they are, then tell me how to fix them
Here is the text:
{questions_text}
"""

def call_gpt(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a UGC NET paper setter."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    print("❌ All retries failed.")
    return ""

def save_to_docx(content, filename="Questions.docx"):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)

# === INPUT HANDLING ===
def get_user_question_plan():
    print("📋 Available Question Types:")
    for i, qtype in enumerate(prompt_templates.keys(), 1):
        print(f"{i}. {qtype}")

    plan = {}
    print("\n✏️ Enter number of questions you want for each type (must be multiple of 5):")
    for qtype in prompt_templates.keys():
        while True:
            try:
                num = int(input(f"How many '{qtype}' questions? "))
                if num < 0:
                    print("❌ Enter a non-negative number.")
                    continue
                if num % CHUNK_SIZE != 0:
                    print(f"⚠️ Must be a multiple of {CHUNK_SIZE}.")
                    continue
                plan[qtype] = num
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    return plan

# === GENERATION ===
def generate_all_prompts_from_plan(plan):
    all_prompts = []
    for qtype, total_questions in plan.items():
        num_chunks = total_questions // CHUNK_SIZE
        print(f"\n🧠 Generating {total_questions} '{qtype}' questions in {num_chunks} chunks...")
        for _ in range(num_chunks):
            topics_chunk = pick_random_topics(CHUNK_SIZE)
            prompt = build_prompt_from_template(topics_chunk, qtype)
            all_prompts.append((qtype, prompt))
    return all_prompts

# === MAIN EXECUTION ===
if __name__ == "__main__":
    user_plan = get_user_question_plan()
    generated_prompts = generate_all_prompts_from_plan(user_plan)
    questions_output = ""
    verification_output = ""
    for qtype, prompt in generated_prompts:
        print(f"{qtype} : {prompt} \n\n")
        # print(f"\n⚙️ Calling GPT for: {qtype}")
        generated_questions = call_gpt(prompt)
        questions_output += generated_questions + "\n\n"
        verification = call_gpt(verify_prompt(generated_questions))
        verification_output += verification + "\n\n"

    save_to_docx(questions_output, "Questions.docx")
    save_to_docx(verification_output, "Verifications.docx")
    print("\n✅ Mock paper generated and saved to Word document.")
