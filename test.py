from google import genai

client = genai.Client(api_key="AIzaSyCDfqF5MJskS3a_33wg_1-xyA46n3eJs2E")

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(res.text)