import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

def generate_study_notes(topic: str, model) -> str:
    prompt = f"""
You are a helpful academic assistant. Generate clear, well-structured study notes on the following topic:

Topic: {topic}

Your study notes must include:
1. A brief overview (2-3 sentences)
2. Key concepts (bullet points)
3. Important definitions (if applicable)
4. A summary (1-2 sentences)

Keep the language simple and suitable for a university student. Be concise but thorough.
"""
    response = model.generate_content(prompt)
    return response.text