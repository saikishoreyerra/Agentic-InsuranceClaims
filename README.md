# ClaimForge AI — Multi-Agent Insurance Adjudication System

Production Python project converted from the ClaimForge Colab notebook. An agentic RAG system built with **LangGraph**, **Groq**, **Chroma DB**, and **Streamlit** to evaluate insurance claims against Indian policy, endorsement, and regulatory documents.

## Features

- Agentic RAG pipeline: retrieve → grade → rewrite → adjudicate
- Tavily web fallback when local policy context is insufficient
- Hallucination / grounding guardrails before final output
- Human escalation for low-confidence or ungrounded decisions
- CLI entry point (`python app.py`) and optional Streamlit UI

## Project structure

```text
.
├── app.py                      # Entry point
├── config/settings.py          # API keys, paths, thresholds
├── schemas/models.py           # Pydantic output schemas
├── prompts/                    # Prompt templates
├── rag/                        # Ingest, retriever, LLM engine, chains, bootstrap
├── nodes/                      # LangGraph node functions
├── graph/                      # State + workflow assembly
├── utils/generate_sample_pdfs.py
├── ui/streamlit_app.py         # Streamlit dashboard
├── data/                       # policies / endorsements / regulations
├── vector_db/                  # Chroma persistence (gitignored)
└── tests/
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # then edit with your API keys
```

Required environment variables:

- `GROQ_API_KEY` — Groq chat model access
- `TAVILY_API_KEY` — web-search fallback
- `LLM_MODEL_NAME` — optional (default: `llama-3.1-8b-instant`)

## Run

```bash
# Interactive CLI adjudication
python app.py

# One-shot claim
python app.py --claim "My home flooded during monsoon; walls need repair under Bharat Griha Raksha."

# Generate sample PDFs / rebuild vector store
python app.py --generate-pdfs
python app.py --ingest

# Streamlit UI
python app.py --ui
```

On first claim run, the app generates sample PDFs (if missing) and builds the Chroma vector store automatically.

## Architecture

```text
User Claim → Retrieve Context → Relevance Grader
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼ (Relevant)                            ▼ (Irrelevant)
            Adjudication                           Rewrite Query
                 │                                       │
                 ▼                                       ▼
        Hallucination Check                      Retry Limit Exceeded?
                 │                                ├─ No  → Retrieve
                 ▼                                └─ Yes → Tavily Web Search
     Confidence & Grounding Pass?                               │
        ├─ Yes → Final Output                                   └→ Adjudication
        └─ No  → Human Escalation
```

## Tests

```bash
python tests/test_rag_adjudication.py
python tests/test_nodes_pipeline.py
```

Ensure PDFs are generated and ingested before running tests.

## Notes

- Colab secrets (`google.colab.userdata`) are replaced by `.env` / environment variables.
- Embedding model remains `all-MiniLM-L6-v2`; the Groq chat model is configured via `LLM_MODEL_NAME` (the notebook incorrectly reused the embedding model id for ChatGroq).
- Placeholder API key values (including those from `.env.example`) are rejected; set real keys before running adjudication.
- `vector_db/.gitkeep` is ignored when deciding whether ingestion is needed.
# Test
