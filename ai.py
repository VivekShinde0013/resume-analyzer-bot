from google import genai

# ✅ Put your VALID API key here
client = genai.Client(api_key="AIzaSyCDfqF5MJskS3a_33wg_1-xyA46n3eJs2E")

def analyze_resume(job_desc, resume_text):

    prompt = f"""
You are an ATS resume expert.

Job Description:
{job_desc}

Candidate Resume:
{resume_text}

Do TWO things:

1. Give detailed analysis:
- Score out of 10
- Matching skills
- Missing skills
- Weak areas
- Suggestions

2. Rewrite SAME resume professionally:
- Keep structure same
- Improve wording
- Add job-specific keywords

OUTPUT FORMAT:

=== ANALYSIS ===
...

=== RESUME ===
...
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # ✅ CORRECT MODEL
            contents=prompt
        )

        text = response.text

        print("GEMINI OUTPUT:\n", text)

        # ✅ Split safely
        if "=== RESUME ===" in text:
            parts = text.split("=== RESUME ===")
            analysis = parts[0].replace("=== ANALYSIS ===", "").strip()
            resume = parts[1].strip()
        else:
            analysis = text
            resume = resume_text

        return analysis, resume

    except Exception as e:
        print("GEMINI ERROR:", e)

        return (
            "Error generating analysis",
            "Error generating resume"
        )