import os
from functools import lru_cache

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config.settings import VECTOR_DB_DIR, EMBEDDING_MODEL_NAME, HF_TOKEN

try:
    import streamlit as st
    _HAS_STREAMLIT = True
except Exception:
    st = None
    _HAS_STREAMLIT = False


def _load_embedding_engine():
    print("🔄 [Retriever] Loading Hugging Face Embedding Engine into cache...")
    hf_token = HF_TOKEN or os.environ.get("HF_TOKEN")
    if _HAS_STREAMLIT and hasattr(st, "secrets"):
        try:
            if "HF_TOKEN" in st.secrets:
                hf_token = st.secrets["HF_TOKEN"]
        except Exception:
            pass

    model_kwargs = {}
    if hf_token:
        model_kwargs["token"] = hf_token

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs=model_kwargs
    )


if _HAS_STREAMLIT:
    get_embedding_engine = st.cache_resource(_load_embedding_engine)
else:
    get_embedding_engine = lru_cache(maxsize=1)(_load_embedding_engine)


def fetch_context(query_text: str = None, query: str = None, top_k: int = 4):
    """
    Fetches context chunks from local Chroma DB.
    Supports both `query` and `query_text` keyword arguments.
    """
    # Resolve argument name variations
    search_query = query_text or query
    if not search_query:
        print("⚠️ [Retriever] Empty query passed to fetch_context.")
        return []

    if not os.path.exists(VECTOR_DB_DIR):
        print(f"⚠️ [Retriever] Directory missing at {VECTOR_DB_DIR}")
        return []

    embedding_engine = get_embedding_engine()
    vector_store = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embedding_engine
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    documents = retriever.invoke(search_query)
    print(f"📄 [Retriever] Found {len(documents)} context chunks for query: '{search_query[:40]}...'")
    return documents
