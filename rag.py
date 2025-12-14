import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ FREE MODEL
model = genai.GenerativeModel("models/gemini-flash-lite-latest")

def generate_answer(question, context_chunks):
    if not context_chunks:
        return "No relevant information found on the website."

    # Build context from retrieved chunks
    context = "\n\n".join(
        [chunk["text"][:500] for chunk in context_chunks]
    )

    prompt = f"""
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not present, say "Information not available".

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text
