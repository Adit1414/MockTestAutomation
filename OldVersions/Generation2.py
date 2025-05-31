import openai
import random
import pandas as pd
from docx import Document
from PromptsDict import prompt_templates  # Load the prompt dictionary

# === CONFIGURATION ===
OPENAI_API_KEY = 'your-openai-api-key'
MODEL = 'gpt-4-turbo'
EXCEL_PATH = 'Comp and Socio Syllabus.xlsx'   # Excel file with a "Topics" column
NUM_QUESTIONS = 10
CHUNK_SIZE = 5
QUESTION_TYPE = "MTF"

# === UTILITIES ===
def pick_random_topics(num=5, excel_path=EXCEL_PATH):
    try:
        df = pd.read_excel(excel_path)
        topic_column = df.columns[0]
        topics = df[topic_column].dropna().tolist()
        if len(topics) < num:
            raise ValueError(f"Only {len(topics)} topics available, but {num} requested.")
        selected = random.sample(topics, num)
        # print("✅ Randomly Selected Topics:")
        # for i, topic in enumerate(selected, 1):
        #     print(f"{i}. {topic}")
        return selected
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def format_topics(topics_list):
    return "\n".join([f"{i+1}. {topic}" for i, topic in enumerate(topics_list)])

def build_prompt_from_template(topics_list, template_key):
    topics_str = format_topics(topics_list)
    template = prompt_templates.get(template_key, "")
    return template.format(topics=topics_str)

def verify_prompt(questions_text):
    return f"""
You are an expert UGC NET evaluator. Please verify the following questions:
- Are the answer keys correct?
- Are the solutions logical?
- Are any options misleading or repeated?
- Are all keywords explained well?
Here is the text:
{questions_text}
"""

def call_gpt(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a UGC NET paper setter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def save_to_docx(content, filename="UGC_NET_Mock.docx"):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)

# === MAIN EXECUTION ===
final_output = ""
for _ in range(NUM_QUESTIONS // CHUNK_SIZE):
    selected_topics = pick_random_topics(num=CHUNK_SIZE)
    generation_prompt = build_prompt_from_template(selected_topics, QUESTION_TYPE)
    generated_questions = call_gpt(generation_prompt)

    verification_prompt = verify_prompt(generated_questions)
    verified_questions = call_gpt(verification_prompt)

    final_output += verified_questions + "\n\n"

save_to_docx(final_output)
print("✅ Mock paper generated and saved to Word document.")


# # testing
# selected_topics = pick_random_topics(num=CHUNK_SIZE)
# generation_prompt = build_prompt_from_template(selected_topics, "MTF")
# print(generation_prompt)