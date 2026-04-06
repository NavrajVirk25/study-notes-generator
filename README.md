# 📝 Study Notes Generator

An AI-powered web app that generates structured study notes on any topic instantly.
Built with Python, Google Gemini 2.0 Flash, and Streamlit.

---

## 📖 Description

Study Notes Generator lets you type any topic and receive clean, structured study notes
in seconds. Notes are generated using Google's Gemini 2.0 Flash AI model and are
formatted into four sections: an overview, key concepts, a real-world example, and
practice questions. Notes can be downloaded as a `.txt` file for offline study.

---

## ✨ Features

- 🧠 AI-generated notes with consistent 4-section structure
- 📌 Overview, Key Concepts, Real-World Example, and Practice Questions
- ⬇️ Download notes as a `.txt` file
- 🕓 Session history — tracks all topics searched in the current session
- ✅ Input validation — rejects empty, gibberish, or symbol-only inputs
- 🔴 Live character counter with warning when nearing the 100-character limit
- 💬 Friendly error messages for API and connection issues

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13.7 | Core programming language |
| Google Gemini 2.0 Flash | AI model for generating study notes (free tier) |
| Streamlit | Web app framework |
| python-dotenv | Loads API key safely from `.env` file |
| pytest | Automated testing framework |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/NavrajVirk25/study-notes-generator.git
cd study-notes-generator
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key
Create a file called `.env` in the project root:
```
GEMINI_API_KEY=your_api_key_here
```
Get a free API key at [aistudio.google.com](https://aistudio.google.com)

> ⚠️ Never share or push your `.env` file. It is already blocked by `.gitignore`.

---

## ▶️ How to Run the App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🧪 How to Run Tests
```bash
pytest test_app.py -v
```

Expected output:
```
14 passed in X.xx secs
```

Tests cover input validation logic and AI API call behaviour.
The Gemini API is mocked during testing — no API key required to run tests.

---

## 🎓 Project Context

Built as a group project for **INFO 4330 — Data Warehousing and Data Mining**
at **Kwantlen Polytechnic University (KPU)**, Spring 2026.
