# 🤖 AI Resume Analyzer Bot

An AI-powered Resume Analyzer that evaluates resumes based on job descriptions and generates a company-ready improved CV. Integrated with Telegram Bot for real-time interaction.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🧠 AI-based Resume Analysis
- 📊 ATS Score (out of 10)
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- 🔍 Detailed Improvement Suggestions
- 📑 Auto-generated Company-ready Resume (PDF)
- 🤖 Telegram Bot Integration

---

## 🛠 Tech Stack

- Python
- Flask (Backend API)
- Telegram Bot API
- Google Gemini AI (LLM)
- FPDF (PDF Generation)

---

## ⚙️ How It Works

1. User sends Job Description
2. Uploads Resume PDF
3. AI analyzes resume vs JD
4. Bot returns:
   - Detailed analysis
   - Improved resume PDF

---

## 📂 Project Structure


---

## 🔧 Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

python app.py

python bot.py

If you like this project, give it a star!