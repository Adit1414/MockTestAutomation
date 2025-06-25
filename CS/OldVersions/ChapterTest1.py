import os
import random
import pandas as pd
from CS.Generation.Generation import main
from PromptsDict import prompt_templates

MODE_OPTIONS = {
    "1": "Full Mock Test (entire syllabus)",
    "2": "Chapter-wise Test (select specific chapters)"
}

CHUNK_SIZE = 3
CHAPTER_XLSX = "CS/ChapterSyllabus.xlsx"  # New chapter-wise file

# === MODE SELECTION ===
def choose_mode():
    print("\n🔧 Choose test generation mode:")
    for key, val in MODE_OPTIONS.items():
        print(f"{key}. {val}")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice in MODE_OPTIONS:
            return choice
        print("❌ Invalid input. Try again.")

# === LOAD CHAPTER-WISE SYLLABUS ===
def load_chapterwise_topics(filepath=CHAPTER_XLSX):
    try:
        df = pd.read_excel(filepath, sheet_name=None)
        # sheet_name=None loads all sheets into a dict
        chapter_topics = {sheet: df[sheet][df[sheet].columns[0]].dropna().tolist() for sheet in df}
        return chapter_topics
    except Exception as e:
        print(f"❌ Failed to load chapter-wise syllabus: {e}")
        return {}

# === ASK WHICH CHAPTERS ===
def choose_chapters(chapter_topics):
    print("\n📘 Available Chapters:")
    chapters = list(chapter_topics.keys())
    for idx, name in enumerate(chapters, 1):
        print(f"{idx}. {name}")

    chosen = []
    print("\n✍️ Enter chapter numbers (comma-separated, e.g., 1,3,5):")
    raw = input().strip()
    try:
        indices = [int(x.strip()) for x in raw.split(",")]
        for i in indices:
            if 1 <= i <= len(chapters):
                chosen.append(chapters[i - 1])
        return chosen
    except:
        print("❌ Invalid input format.")
        return []

# === RANDOMIZE QUESTION TYPES ===
def randomize_qtypes(prompt_dict, num=3):
    return random.choices(list(prompt_dict.keys()), k=num)

# === MOCK MAIN FLOW ===
if __name__ == "__main__":
    mode = choose_mode()

    if mode == "1":
        print("\n🧪 Starting Full Mock Test Mode...")
        main()

    elif mode == "2":
        print("\n📘 Starting Chapter Test Mode...")
        chapters_data = load_chapterwise_topics()

        if not chapters_data:
            print("❌ Aborting chapter test mode due to load error.")
            exit(1)

        selected_chapters = choose_chapters(chapters_data)

        if not selected_chapters:
            print("❌ No chapters selected. Aborting.")
            exit(1)

        for chapter in selected_chapters:
            topics = chapters_data[chapter]
            print(f"\n🧠 Generating 15 questions for chapter: {chapter}")
            qtypes = randomize_qtypes(prompt_templates, num=15)

            for i in range(0, 15, CHUNK_SIZE):
                chunk_topics = topics[i:i+CHUNK_SIZE]
                if len(chunk_topics) < CHUNK_SIZE:
                    print(f"⚠️ Skipping final short chunk in {chapter}.")
                    continue
                selected_qtype = qtypes[i // CHUNK_SIZE]
                prompt = build_prompt_from_template(chunk_topics, selected_qtype)
                print(f"\nPrompt ({selected_qtype}) for {chapter}:")
                print(prompt)
                # Call GPT here in real implementation

