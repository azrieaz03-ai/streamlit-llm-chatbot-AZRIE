# utils.py
# NOTE: This template supports multiple backends. 
# Replace 'mock' functions with real LangChain/OpenAI calls when integrating for real.

from typing import List, Optional

def retrieve_documents(query: str) -> List[dict]:
    """Mock retrieval function. 
    In production, query your vector DB and return top docs.
    Example return format: list of {'id':..., 'text':..., 'score':...}
    """
    return [
        {"id": "doc1", "text": "Tips manajemen waktu: gunakan teknik Pomodoro.", "score": 0.95},
    ]


def generate_response(
    user_input: str,
    docs: Optional[List[dict]] = None,
    style: str = "Santai",
    temperature: float = 0.3,
    max_tokens: int = 350,
    use_agent: bool = True,
) -> str:
    """Mock LLM generator. 
    Replace with real LLM API calls (OpenAI, Anthropic, etc.) or LangChain chains.
    """

    # Build prompt with optional retrieved context
    prompt_parts = []
    if docs:
        prompt_parts.append("Retrieved documents:\n")
        for d in docs:
            prompt_parts.append(f"- {d['text']}\n")
        prompt_parts.append("User request:\n" + user_input + "\n")

    # Style influence
    if style == "Formal":
        tone = "Tolong jawab secara profesional dan ringkas."
    else:
        tone = "Jawab dengan gaya santai dan ramah."

    prompt_parts.append("Tone: " + tone)
    prompt = "\n".join(prompt_parts)

    # Mocked generation: in practice call model here.
    # Example: call OpenAI ChatCompletion or LangChain LLM chain
    # e.g., llm = OpenAI(temperature=temperature, max_tokens=max_tokens)
    # answer = llm(prompt)

    # For the template, return a deterministic mock response
    answer = (
        "Berikut saran untukmu: Gunakan teknik Pomodoro (25/5), "
        "prioritaskan 3 tugas teratas, dan cek kalender untuk deadline."
    )

    if use_agent and "buatkan event" in user_input.lower():
        # Mock agent action
        answer += "\n\n[Agent] Event telah dibuat (mock)."

    return answer
