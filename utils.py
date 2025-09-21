import os
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv

# =========================
# Load API Key
# =========================
load_dotenv("api.env")  # baca dari file api.env

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY tidak ditemukan. Pastikan ada di api.env")

# 🔑 Konfigurasi Gemini
genai.configure(api_key=API_KEY)


# =========================
# Retrieval Mock
# =========================
def retrieve_documents(query: str) -> List[dict]:
    """Mock retrieval function. In production, query your vector DB and return top docs."""
    return [
        {"id": "doc1", "text": "Tips manajemen waktu: gunakan teknik Pomodoro.", "score": 0.95},
    ]


# =========================
# Generate Response
# =========================
def generate_response(
    user_input: str,
    history: Optional[List[dict]] = None,   # 🆕 riwayat percakapan
    docs: Optional[List[dict]] = None,
    style: str = "Santai",
    temperature: float = 0.3,
    max_tokens: int = 350,
    use_agent: bool = True,
) -> str:
    """Generate response multi-turn menggunakan Google Gemini API"""

    prompt_parts = []

    # Jika ada dokumen relevan (RAG)
    if docs:
        prompt_parts.append("Retrieved documents:\n")
        for d in docs:
            prompt_parts.append(f"- {d['text']}\n")

    # Tambahkan riwayat percakapan
    if history:
        prompt_parts.append("Conversation history:\n")
        for msg in history:
            role = "User" if msg["role"] == "user" else "Assistant"
            prompt_parts.append(f"{role}: {msg['content']}\n")

    # Tambahkan pertanyaan terbaru
    prompt_parts.append("User request:\n" + user_input + "\n")

    # Tambahkan gaya bahasa
    if style == "Formal":
        tone = "Tolong jawab secara profesional, terstruktur, dan ringkas."
    else:
        tone = "Jawab dengan gaya santai, ramah, dan mudah dipahami."

    prompt_parts.append("Tone: " + tone)

    # Gabungkan prompt
    prompt = "\n".join(prompt_parts)

    # 🔍 Debug (optional)
    print("\n=== PROMPT KE GEMINI ===")
    print(prompt)
    print("========================\n")

    # Panggil Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        },
    )

    answer = response.text if hasattr(response, "text") and response.text else "Maaf, tidak ada jawaban."

    # Agent mock (opsional)
    if use_agent and "buatkan event" in user_input.lower():
        answer += "\n\n[Agent] Event telah dibuat (mock)."

    return answer
