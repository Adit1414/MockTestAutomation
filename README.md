# 🧠 UGC NET Mock Question Generator

A Python-based tool to **automatically generate**, **verify**, and **save** high-quality UGC NET-style mock questions using OpenAI’s `gpt-4-turbo` model. Supports multiple question types like **Assertion-Reasoning**, **Match the Following**, and more — with built-in topic randomization, error checking, and Word document export.

---

## ✨ Features

* ✅ **Randomized topic selection** from an Excel syllabus file
* 🧩 **Prompt templates** for various question types
* 🤖 **ChatGPT (gpt-4-turbo)** integration to generate and verify questions
* 🔍 **Automated verification** of answer keys and solutions for accuracy
* 📄 **Exports** final questions and verification reports to `.docx` files
* 🔁 Generates questions in **batches of 5** (configurable)

---

## 📁 Project Structure

```
├── main.py                 # Main script to run the generator
├── PromptsDict.py          # Dictionary of prompt templates
├── Book1.xlsx              # Excel file containing syllabus topics
├── Questions.docx          # Output file with generated questions
├── Verifications.docx      # Output file with verification responses
└── README.md               # This file
```

---

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install openai pandas python-docx
```

You also need:

* Python 3.8+
* An [OpenAI API key](https://platform.openai.com/account/api-keys)

---

## 🔐 Setup

1. **Set your API key** (temporary):

   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

   Or permanently (on Linux/macOS):

   ```bash
   echo 'export OPENAI_API_KEY="your-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```

2. **Prepare your syllabus Excel file**

   * Place it as `Book1.xlsx`
   * The first column should contain the topic names (one per row)

---

## 🚀 How to Run

```bash
python main.py
```

You’ll be prompted to enter how many questions you want for each available type (in multiples of 5).

The script will:

* Pick random topics from the Excel file
* Generate and verify question batches using ChatGPT
* Save the final content into `Questions.docx` and `Verifications.docx`

---

## 🧩 Supported Question Types

All prompt types are loaded from `PromptsDict.py`. Example keys you can customize:

* `Assertion-Reasoning`
* `Match-the-Following`
* `Multiple-Choice-Difficult`
* *(Add your own!)*

---

## 📌 Configuration

You can customize:

* `CHUNK_SIZE = 5` – How many questions per batch
* `MODEL = "gpt-4-turbo"` – Which model to use
* Prompt templates in `PromptsDict.py`

---

## 📤 Sample Prompt Template (PromptsDict.py)

```python
prompt_templates = {
    "Assertion-Reasoning": """
Create 5 Assertion and Reasoning type questions from the following topics:
{topics}

Each question must include:
- Assertion (A)
- Reason (R)
- Four options (1 to 4)
- Correct answer and detailed solution

Answer Key: {answer_key}
"""
}
```

---

## 📚 Example Output

The final `.docx` files will contain:

* ✅ 5 or more fully formed questions
* 🧐 A detailed verification report checking:

  * Accuracy of answers
  * Logical consistency of solutions
  * Whether any option is misleading or repeated

---

## 🤖 GPT Model Info

Uses:

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4-turbo"
```

Which gives access to OpenAI’s **latest GPT-4.1** capabilities.

---

## 🧠 Future Enhancements

* [ ] GUI with streamlit or tkinter
* [ ] Export to PDF
* [ ] Fine-tuned model integration

---
