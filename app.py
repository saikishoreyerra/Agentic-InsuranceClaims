"""
ClaimForge AI — application entry point.

Usage:
    python app.py
    python app.py --claim "My home flooded during monsoon..."
    python app.py --ui
    python app.py --generate-pdfs
    python app.py --ingest
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# Ensure project root is on sys.path when launched as `python app.py`
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def run_claim(claim: str) -> dict:
    """Invoke the compiled LangGraph adjudication workflow for a claim."""
    from rag.bootstrap import ensure_vector_store
    from graph.workflow import app_engine

    status = ensure_vector_store(generate_pdfs_if_missing=True)
    if status.startswith("ERROR"):
        raise RuntimeError(status)

    inputs = {
        "claim": claim,
        "query": None,
        "documents": [],
        "retry_count": 0,
        "relevance": "no",
        "decision": "Pending",
        "confidence": 0.0,
        "final_answer": "",
        "hallucination": None,
        "evidence_citations": [],
        "audit_trail": ["Workflow initialized via CLI entry point."],
    }
    return app_engine.invoke(inputs)


def print_result(state: dict) -> None:
    decision = state.get("decision", "Escalate")
    confidence = state.get("confidence", 0.0)
    explanation = state.get("final_answer", "N/A")
    logs = state.get("audit_trail", [])

    print("\n" + "=" * 69)
    print("FINAL ADJUDICATION RESULT")
    print("=" * 69)
    print(f"Decision    : {decision}")
    print(f"Confidence  : {confidence}")
    print(f"Explanation : {explanation}")
    print("\nAudit Trail:")
    for idx, step in enumerate(logs):
        print(f"  [{idx + 1}] {step}")
    print("=" * 69)


def launch_ui() -> None:
    """Launch the Streamlit adjudication dashboard."""
    from rag.bootstrap import ensure_vector_store

    status = ensure_vector_store(generate_pdfs_if_missing=True)
    if status.startswith("ERROR"):
        raise RuntimeError(status)

    ui_path = PROJECT_ROOT / "ui" / "streamlit_app.py"
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(ui_path)],
        check=True,
        cwd=str(PROJECT_ROOT),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ClaimForge AI — multi-agent insurance claim adjudication"
    )
    parser.add_argument(
        "--claim",
        type=str,
        help="Claim statement to adjudicate",
    )
    parser.add_argument(
        "--ui",
        action="store_true",
        help="Launch the Streamlit dashboard",
    )
    parser.add_argument(
        "--generate-pdfs",
        action="store_true",
        help="Generate sample Indian insurance PDF documents",
    )
    parser.add_argument(
        "--ingest",
        action="store_true",
        help="Ingest PDFs from data/ into the Chroma vector store",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.generate_pdfs:
        from utils.generate_sample_pdfs import generate_all_sample_pdfs

        generate_all_sample_pdfs()
        return

    if args.ingest:
        from rag.ingest import run_ingestion

        run_ingestion()
        return

    if args.ui:
        launch_ui()
        return

    claim = args.claim
    if not claim:
        print("ClaimForge AI — Insurance Claims Adjudication Agent")
        print("Enter a claim statement (or pass --claim / --ui):\n")
        claim = input("Claim> ").strip()

    if not claim:
        print("No claim provided. Exiting.")
        sys.exit(1)

    result = run_claim(claim)
    print_result(result)


if __name__ == "__main__":
    main()
