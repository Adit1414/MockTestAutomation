import random
import pandas as pd
from PromptsDict import prompt_templates

# === CONFIGURATION ===
EXCEL_PATH = "Comp and Socio Syllabus.xlsx"
CHUNK_SIZE = 5

# === FUNCTIONS FROM YOU ===
def pick_random_topics(num=5, excel_path=EXCEL_PATH):
    try:
        df = pd.read_excel(excel_path)
        topic_column = df.columns[0]
        topics = df[topic_column].dropna().tolist()
        if len(topics) < num:
            raise ValueError(f"Only {len(topics)} topics available, but {num} requested.")
        selected = random.sample(topics, num)
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

# === STEP 1: Ask for user input ===
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

# === STEP 2: Generate all prompts ===
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

# === MAIN TEST RUN ===
if __name__ == "__main__":
    user_plan = get_user_question_plan()
    generated_prompts = generate_all_prompts_from_plan(user_plan)

    print("\n\n===== 🧾 FINAL PROMPTS GENERATED =====")
    for i, (qtype, prompt) in enumerate(generated_prompts, 1):
        print(f"\n--- Prompt {i} ({qtype}) ---\n")
        print(prompt)
        print("-" * 60)
