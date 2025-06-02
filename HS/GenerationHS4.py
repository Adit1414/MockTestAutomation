from openai import OpenAI
import random
import time
import os
import pandas as pd
from docx import Document
from PromptsDictHS import prompt_templates  # Load the prompt dictionary

# === CONFIGURATION ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = 'gpt-4-turbo'
EXCEL_PATH = "D:\\aditya data\\Freelance Projects\\Automation\\HS\\SyllabusHS.xlsx"
CHUNK_SIZE = 5

# === UTILITIES ===
def load_all_topics(excel_path=EXCEL_PATH):
    try:
        df = pd.read_excel(excel_path)
        topic_column = df.columns[0]
        topics = df[topic_column].dropna().tolist()
        random.shuffle(topics)
        return topics
    except Exception as e:
        print(f"❌ Error loading topics: {e}")
        return []

def validate_topic_capacity(plan, total_topics):
    total_chunks_requested = sum(num // CHUNK_SIZE for num in plan.values())
    if total_chunks_requested > len(total_topics) // CHUNK_SIZE:
        print(f"❌ Not enough unique topics to generate all question chunks without duplication.")
        print(f"💡 Topics available: {len(total_topics)}, Questions requested: {total_chunks_requested * CHUNK_SIZE}")
        exit(1)


def format_topics(topics_list):
    return "\n".join([f"{i+1}. {topic}" for i, topic in enumerate(topics_list)]) 

def build_prompt_from_template(topics_list, template_key):
    topics_str = format_topics(topics_list)
    randomized_answer_key = ', '.join(str(n) for n in random.choices(range(1, 5), k=5))
    template = prompt_templates.get(template_key, "")
    return template.format(topics=topics_str, answer_key=randomized_answer_key)

def verify_prompt(questions_text):
    return f"""
VERIFICATION: Verify these questions 50 times ie. run the instruction 50 times completely. 
Check for any discrepancies or issues with the question, answer key and solutions. 
Check if any options are wrongly marked or any options are similar to each other. 
If everything is correct and doesnt need to be changed, then just say that its all correct and dont explain anything else. 
If anything is to be changed, give me the whole question, answer key, solution rewritten with the same exact format 
and also tell me at the end what went wrong there. 
Example format for verifying
Question 1 - Correct
Question 2 - Correct
Question 3 - INCORRECT - ANSWER KEY MISMATCH
Question 4 - Correct
Question 5 - Correct
<Rewritten Version of the incorrect question - whole question, answer and solution of any incorrect questions>

this is only an example, be completely unbiased in determining the correctness and incorrectness. check and recheck multiple times the correctness
Here are the questions:
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

def save_to_docx(content, filename="QuestionsHS.docx"):
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
def generate_all_prompts_from_plan(plan, all_topics):
    all_prompts = []
    topic_index = 0

    for qtype, total_questions in plan.items():
        num_chunks = total_questions // CHUNK_SIZE
        print(f"\n🧠 Generating {total_questions} '{qtype}' questions in {num_chunks} chunks...")
        for _ in range(num_chunks):
            topics_chunk = all_topics[topic_index: topic_index + CHUNK_SIZE]
            topic_index += CHUNK_SIZE
            prompt = build_prompt_from_template(topics_chunk, qtype)
            all_prompts.append((qtype, prompt))
    return all_prompts


# === MAIN EXECUTION ===
if __name__ == "__main__":
    user_plan = get_user_question_plan()
    all_topics = load_all_topics()
    validate_topic_capacity(user_plan, all_topics)
    generated_prompts = generate_all_prompts_from_plan(user_plan, all_topics)

    questions_output = ""
    verification_output = ""

    for qtype, prompt in generated_prompts:
        print(f"{qtype} : {prompt} \n\n")
        
        # # Actual
        # generated_questions = call_gpt(prompt)
        # questions_output += generated_questions + "\n\n"
        # verification = call_gpt(verify_prompt(generated_questions))
        # verification_output += verification + "\n\n"
        
        # Testing
        questions_output += "generated_questions" + "\n\n"
        verification_output += "verification" + "\n\n"

    save_to_docx(questions_output, "D:\\aditya data\\Freelance Projects\\Automation\\HS\\QuestionsHS.docx")
    save_to_docx(verification_output, "D:\\aditya data\\Freelance Projects\\Automation\\HS\\VerificationsHS.docx")
    print("\n✅ Mock paper generated and saved to Word document.")

