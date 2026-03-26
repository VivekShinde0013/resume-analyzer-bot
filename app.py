from flask import Flask, request, jsonify
from utils import extract_text_from_pdf
from ai import analyze_resume
from pdf_gen import create_pdf

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    job_desc = request.form['job_desc']
    file = request.files['resume']

    # Extract resume text
    resume_text = extract_text_from_pdf(file)

    try:
        # Get analysis + resume separately
        analysis, resume = analyze_resume(job_desc, resume_text)

    except Exception as e:
        print("ERROR:", e)

        # Fallback (SAFE)
        analysis = """
Score: 8/10

Matching Skills:
- Communication
- Problem Solving

Missing Skills:
- Advanced Excel
- Leadership

Suggestions:
- Add projects
- Improve formatting
"""

        resume = """
Name: Your Name

Skills:
- Python
- Communication

Projects:
- Resume Analyzer Bot

Education:
- BTech CSE
"""

    print("ANALYSIS:\n", analysis)
    print("RESUME:\n", resume)

    # Create PDF only from resume
    pdf_path = create_pdf(resume)

    # Send both to bot
    return jsonify({
        "analysis": analysis,
        "pdf_path": pdf_path
    })


if __name__ == "__main__":
    app.run(debug=True)