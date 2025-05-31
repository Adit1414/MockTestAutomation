import openai
import random
import pandas as pd
from docx import Document
from PromptsDict import prompt_templates


# === CONFIGURATION ===
OPENAI_API_KEY = 'your-openai-api-key'
MODEL = 'gpt-4-turbo'
EXCEL_PATH = 'Comp and Socio Syllabus.xlsx'   # Excel file with a "Topics" column
NUM_QUESTIONS = 10
CHUNK_SIZE = 5
QUESTION_TYPE = '2-statement type'

# === UTILITIES ===
def pick_random_topics(num=5, excel_path=EXCEL_PATH):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_path)

        # Get the first column (assuming it holds all the topics)
        topic_column = df.columns[0]
        topics = df[topic_column].dropna().tolist()

        # Check if enough topics exist
        if len(topics) < num:
            raise ValueError(f"Only {len(topics)} topics available, but {num} requested.")

        # Pick random topics
        selected = random.sample(topics, num)

        # Print the results
        print("✅ Randomly Selected Topics:")
        for i, topic in enumerate(selected, 1):
            print(f"{i}. {topic}")

        return selected

    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def build_prompt(topics_chunk):
    topics_text = ", ".join(topics_chunk)
    return f"""
2 statement type
Topics: {topics_text}
Difficulty: EXTREMELY HARD, EXTREMELY ANALYTICAL
Each question should be unique and not follow a fixed pattern.
Use this exact format:
Example:
67. Consider the following two statements:
Statement I: ...
Statement II: ...
In light of the above statements, choose the correct answer from the options given below:
(1) ...
(2) ...
(3) ...
(4) ...
Answer Key: 1
Solution:
• I(Correct): ...
• II(Correct): ...
Hence, Option (1) is the right answer.
"""

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
    selected_topics = pick_random_topics()
    generation_prompt = build_prompt(selected_topics)
    generated_questions = call_gpt(generation_prompt)

    verification_prompt = verify_prompt(generated_questions)
    verified_questions = call_gpt(verification_prompt)

    final_output += verified_questions + "\n\n"

save_to_docx(final_output)
print("Mock paper generated and saved to Word document.")
