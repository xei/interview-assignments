from google import genai
import os

client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a 100 words"
)

print(response.text)