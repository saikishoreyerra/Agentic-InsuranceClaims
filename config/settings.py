from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# Project roots
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
VECTOR_DB_DIR = str(PROJECT_ROOT / "vector_db")

# Placeholder values that must not be treated as real credentials
_PLACEHOLDER_VALUES = {
    "",
    "your_groq_api_key_here",
    "your_tavily_api_key_here",
    "naya",
    "tavily_key",
}


def _clean_secret(value: str | None) -> str:
    if value is None:
        return ""
    cleaned = value.strip()
    if cleaned in _PLACEHOLDER_VALUES:
        return ""
    return cleaned


# Centralized API Keys configuration
GROQ_API_KEY = _clean_secret(os.getenv("GROQ_API_KEY", ""))
TAVILY_API_KEY = _clean_secret(os.getenv("TAVILY_API_KEY", ""))
HF_TOKEN = _clean_secret(os.getenv("HF_TOKEN", ""))

# RAG Threshold Configurations
RETRY_LIMIT = 2
CONFIDENCE_THRESHOLD = 0.70
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
# Groq chat model (notebook incorrectly used the embedding model id for ChatGroq)
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "llama-3.1-8b-instant")

print("⚙️ Configuration keys loaded successfully.")


def require_groq_api_key() -> str:
    """Return a usable Groq API key or raise a clear configuration error."""
    api_key = GROQ_API_KEY or _clean_secret(os.environ.get("GROQ_API_KEY", ""))
    if not api_key:
        raise ValueError(
            "Missing GROQ_API_KEY. Set a real key in your environment or .env file "
            "(see .env.example)."
        )
    os.environ["GROQ_API_KEY"] = api_key
    return api_key


def require_tavily_api_key() -> str:
    """Return a usable Tavily API key or raise a clear configuration error."""
    api_key = TAVILY_API_KEY or _clean_secret(os.environ.get("TAVILY_API_KEY", ""))
    if not api_key:
        raise ValueError(
            "Missing TAVILY_API_KEY. Set a real key in your environment or .env file "
            "(see .env.example)."
        )
    return api_key
