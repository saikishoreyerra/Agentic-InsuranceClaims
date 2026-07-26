"""Shared helpers for vector-store lifecycle checks and bootstrap."""

from __future__ import annotations

from pathlib import Path

from config.settings import DATA_DIR, VECTOR_DB_DIR


def _is_ignored_store_entry(name: str) -> bool:
    return name.startswith(".") or name == ".gitkeep"


def is_vector_store_ready(vector_db_dir: str | None = None) -> bool:
    """
    Return True when the Chroma persist directory looks initialized.

    Ignores placeholder files such as `.gitkeep` so an empty tracked folder
    is still treated as needing ingestion.
    """
    path = Path(vector_db_dir or VECTOR_DB_DIR)
    if not path.exists() or not path.is_dir():
        return False

    for entry in path.iterdir():
        if not _is_ignored_store_entry(entry.name):
            return True
    return False


def ensure_sample_pdfs() -> None:
    """Generate sample PDFs when the policies directory has none."""
    policy_dir = DATA_DIR / "policies"
    has_pdfs = policy_dir.exists() and any(policy_dir.glob("*.pdf"))
    if not has_pdfs:
        print("No sample PDFs found — generating localized insurance documents...")
        from utils.generate_sample_pdfs import generate_all_sample_pdfs

        generate_all_sample_pdfs()


def ensure_vector_store(generate_pdfs_if_missing: bool = True) -> str:
    """
    Ensure sample documents exist and the Chroma store is ingested.

    Returns a status string: "EXISTS", "SUCCESS", or "ERROR: ...".
    """
    try:
        if generate_pdfs_if_missing:
            ensure_sample_pdfs()

        if is_vector_store_ready(VECTOR_DB_DIR):
            return "EXISTS"

        print("Vector store empty — running document ingestion...")
        from rag.ingest import run_ingestion

        run_ingestion()
        return "SUCCESS"
    except Exception as e:
        return f"ERROR: {str(e)}"
