import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Check your .env file.")
    return genai.Client(api_key=api_key)

def is_valid_topic(topic: str) -> bool:
    import re
    topic = topic.strip()

    # Too short
    if len(topic) < 3:
        return False

    # Must contain at least 2 letters
    if len(re.findall(r'[a-zA-Z]', topic)) < 2:
        return False

    # Reject if more than 50% of characters are non-alphanumeric
    non_alnum = len(re.findall(r'[^a-zA-Z0-9\s]', topic))
    if non_alnum / len(topic) > 0.5:
        return False

    # Reject repeated characters like "aaaaaaa" or "asdfasdf"
    if re.fullmatch(r'(.)\1{3,}', topic):
        return False

    return True

def generate_study_notes(topic: str) -> str:
    client = get_client()

    prompt = f"""You are a knowledgeable and clear academic tutor.

Generate structured study notes on the following topic: "{topic}"

Your response must include:
1. A brief overview (2–3 sentences) explaining what this topic is
2. Key concepts — list the 4–6 most important ideas, each with a short explanation
3. A real-world example that illustrates the topic
4. 3 practice questions to test understanding (no answers needed)

Format your response with clear headings for each section.
Keep the language simple and student-friendly."""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text