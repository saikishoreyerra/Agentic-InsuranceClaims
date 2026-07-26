import os
from langchain_groq import ChatGroq

from config.settings import LLM_MODEL_NAME, require_groq_api_key


def get_llm_engine():
    """
    Initializes a deterministic LLM instance hosted via Groq
    for strict, high-fidelity insurance adjudication reasoning.
    """
    require_groq_api_key()

    return ChatGroq(
        model=LLM_MODEL_NAME,
        temperature=0.0,
    )


if __name__ == "__main__":
    llm = get_llm_engine()
    model_label = getattr(llm, "model_name", None) or getattr(llm, "model", LLM_MODEL_NAME)
    print(f"🚀 Core LLM Engine Successfully Verified: {model_label}")
