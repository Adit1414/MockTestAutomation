# 🧠 MockTestAutomation

An advanced automation system for generating **UGC-NET style mock tests** using the OpenAI GPT API. It supports multiple question formats (MCQ, MTF, Assertion-Reason, etc.) and handles topic selection, formatting, verification, shuffling, and storage — all from a single CLI-based flow.

Supports both:
- **CS**: Computer Science mock tests
- **HS**: Home Science mock tests

---

## ✨ Features

- 📚 Takes topics from a syllabus Excel file (`Syllabus.xlsx`)
- 🤖 Generates questions in batches of 5 using GPT-4 Turbo
- ✅ Verifies answers and solutions via a second GPT pass
- 🔀 Randomizes question order for realism
- 💾 Saves:
  - Final questions: `Questions.docx`
  - Verifications: `Verifications.docx`
  - All raw outputs: `RawResponses/`
  - Skipped or faulty chunks: `Skipped.docx`
- 🔔 Plays sound alerts on success (`CorrectHarp.wav`) or failure (`WrongBuzzer.wav`)
- 🛠️ Supports both **CS** and **HS** domains via separate prompt/template files

---

## 🏗 Project Structure

```
MockTestAutomation/
├── CorrectHarp.wav               # Success chime
├── WrongBuzzer.wav              # Error chime
├── TokenCalculator.py           # Cost estimation utility
├── CS/
│   ├── Generation.py            # Main driver script for CS
│   ├── PromptsDict.py           # Prompt templates for CS
│   ├── Syllabus.xlsx            # List of CS topics
│   ├── Questions.docx           # Final generated questions
│   ├── Verifications.docx       # GPT verification results
│   ├── Skipped.docx             # Faulty/incomplete question chunks
│   ├── QSave.docx               # Combined Q&A with solutions
│   ├── RawResponses/            # All raw GPT outputs
│   │   └── gpt_response_*.docx
│   └── Test.py                  # Experimental script
├── HS/
│   ├── GenerationHS.py          # Main driver script for HS
│   ├── PromptsDictHS.py         # Prompt templates for HS
│   ├── SyllabusHS.xlsx
│   ├── QuestionsHS.docx
│   ├── VerificationsHS.docx
│   ├── SkippedHS.docx
│   ├── QSaveHS.docx
│   └── RawResponses/
│       └── gpt_response_*.docx
```

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.10+
- Windows OS (uses `winsound`)
- OpenAI API Key (add via `.env` or system environment variable `OPENAI_API_KEY`)
- Packages:
  ```bash
  pip install openai pandas python-docx
  ```
---

## 🧪 Usage

Run the generator script for CS or HS:

```bash
cd CS
python Generation.py

or

cd HS
python GenerationHS.py
```

Choose your question types and quantity (in multiples of 5). Everything else is automatic:
- GPT generates, formats, and saves output
- Errors (e.g., if GPT returns <5 questions) are logged and skipped
- Raw GPT output is always saved in `RawResponses/` for inspection

---

## 📌 Upcoming Features

- 📚 **Chapter Test Automation**  
  Select any chapter or portion of the syllabus and generate a full-length mock test using **only** those topics.

- 🌐 **Generalized Subject Support**  
  Move beyond CS and HS, and even UGC NET — input **any custom syllabus Excel file** and generate questions regardless of subject area or exam.  
  (e.g., Sociology, Economics, Psychology, Mathematics etc.)

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
- **No additional restrictions** — You may not apply legal terms or technological measures that restrict others.

🔗 Full license text: [https://creativecommons.org/licenses/by-nc/4.0/legalcode](https://creativecommons.org/licenses/by-nc/4.0/legalcode)

---

## 🙌 Acknowledgements

- Developed with love and late-night debugging 💻☕
