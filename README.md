# 🧠 MockTestAutomation

A highly customizable CLI-based automation system to generate **Objective-style mock tests** (e.g., UGC-NET, SSC, GATE, etc.) using the OpenAI GPT API. It supports multiple question formats (MCQ, MTF, Assertion-Reason, etc.), and handles topic selection, prompt generation, response verification, shuffling, and output formatting — all with minimal setup.

The system currently includes ready-to-use setups for **UGC NET Computer Science**, but can easily be adapted to any subject or exam.

---

## ✨ Features

- 📚 Pulls topics from a user-defined syllabus Excel file
- 🤖 Supports both:
  - **Full-length mock tests** (random topics)
  - **Chapter-wise tests** (topic-constrained)
- 🎯 Generates diverse question formats from templates using GPT-4 Turbo
- ✅ Double-verification: auto-checks questions, answer keys, and logic via GPT
- 🔀 Randomizes question order for realism
- 💾 Saves:
  - Final questions: `Questions.docx`
  - Verifications: `Verifications.docx`
  - All raw outputs: `RawResponses/`
  - Skipped/faulty chunks: `Skipped.docx`
- 🔔 Plays sound alerts for success (`CorrectHarp.wav`) and error (`WrongBuzzer.wav`)
- 🔄 Easily extensible to **any subject or syllabus** for **any objective type exam**

---

## 🏗 Project Structure

```
MockTestAutomation/
├── CorrectHarp.wav                # Success sound
├── WrongBuzzer.wav                # Error sound
├── TokenCalculator.py             # Estimate token usage (optional)
├── README.md
├── LICENSE
├── src/
│   ├── Generation.py              # Full-length test generator
│   ├── PromptsDict.py             # Prompt templates for full tests
│   ├── ChapterTest.py             # Chapter-wise test generator
│   ├── ChapterPromptsDict.py      # Prompt templates for chapter tests
│   ├── Gen/
│   │   ├── Syllabus.xlsx              # Your full syllabus (1st column only)
│   │   ├── Questions.docx             # Saved final questions
│   │   ├── Verifications.docx         # GPT verification output
│   │   ├── Skipped.docx               # Incomplete chunks
│   ├── Chapter/
│   │   ├── ChapterSyllabus.xlsx       # Topics arranged column-wise (1 chapter = 1 column, 1st row is chapter name)
│   │   ├── ChapterQuestions.docx
│   │   ├── ChapterVerifications.docx
│   │   ├── ChapterSkipped.docx
│   ├── RawResponses/
│       └── gpt_response_*.docx        # All raw GPT outputs saved by timestamp
```

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.10+
- Windows OS (uses `winsound`)
- OpenAI API Key (set as environment variable: `OPENAI_API_KEY`)
- Install dependencies:

```bash
pip install openai pandas python-docx
```

---

## 🧪 Usage

### 🔹 Full-Length Mock Test (Random Topics)
```bash
cd src
python Generation.py
```
- Select question types and how many of each (multiples of 5).
- GPT will auto-generate prompts, questions, verify, and save.

---

### 🔸 Chapter-Wise Test (Fixed Topics)
```bash
cd src
python ChapterTest.py
```
- Select chapters from `ChapterSyllabus.xlsx`
- Each chapter must have **exactly 15 topics** listed **column-wise**
- First row should be chapter names; rows 2–16 should be topics.

---

## 📚 Customize for Any Subject or Exam

- **Want to use your own syllabus?**
  - For full tests: replace `Gen/Syllabus.xlsx` with your list of topics (1st column only).
  - For chapter tests: update `Chapter/ChapterSyllabus.xlsx` using the column format.

- The system is built to support **any objective-style exam**:
  - UGC NET (e.g., Sociology, Commerce, Psychology)
  - JEE Mains, NEET, etc
  - SSC, Banking, GATE, CSAT, etc.
  - Custom corporate aptitude tests

---

## 📌 Upcoming Features

- 🧠 **Smarter prompt variation based on subject or exam type**
- 🔢 **Integration of Questions and Verifications**
- 🌍 **Export to PDF + HTML for easier distribution**

---

## 📄 License

This project is licensed under:

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

**Under the following terms:**
- **Attribution** — You must give appropriate credit.
- **NonCommercial** — You may not use the material for commercial purposes.

🔗 Full license text: [https://creativecommons.org/licenses/by-nc/4.0/legalcode](https://creativecommons.org/licenses/by-nc/4.0/legalcode)

---

## 🙌 Acknowledgements

- Built with late-night logic and caffeine ☕