# ClaimForge AI — Multi-Agent Insurance Adjudication System

A production-ready **Agentic Retrieval-Augmented Generation (RAG)** system for automated insurance claim adjudication. Built using **LangGraph**, **Groq LLM**, **ChromaDB**, and **Streamlit**, the system evaluates insurance claims against Indian insurance policy documents, endorsements, and regulatory guidelines.

---

## Features

- Multi-Agent RAG workflow using LangGraph
- Intelligent document retrieval using ChromaDB
- Query rewriting for improved retrieval accuracy
- Tavily web search fallback when local context is insufficient
- Hallucination detection and grounding verification
- Human escalation for low-confidence decisions
- Interactive CLI and Streamlit web interface
- Automatic PDF ingestion and vector database creation

---

# Project Structure

```text
.
├── app.py                      # Main application entry point
├── config/
│   └── settings.py             # Configuration and API settings
├── schemas/
│   └── models.py               # Pydantic schemas
├── prompts/                    # Prompt templates
├── rag/                        # RAG engine and retriever
├── nodes/                      # LangGraph nodes
├── graph/                      # Workflow graph
├── ui/
│   └── streamlit_app.py        # Streamlit UI
├── utils/
│   └── generate_sample_pdfs.py
├── data/                       # Insurance documents
├── vector_db/                  # Chroma Vector Database
├── tests/                      # Test cases
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Prerequisites

Before starting, ensure you have:

- Python **3.12**
- Git
- A Groq API Key
- A Tavily API Key

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/saikishoreyerra/Agentic-InsuranceClaims
cd Agentic-InsuranceClaims
```

---

## 2. Create a Virtual Environment

```bash
python3.12 -m venv .venv
```

---

## 3. Activate the Virtual Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 4. Upgrade pip

```bash
pip install --upgrade pip
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Configure Environment Variables

Copy the sample environment file.

### macOS / Linux

```bash
cp .env.example .env
```

### Windows

```cmd
copy .env.example .env
```

Open the `.env` file and add your API keys.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

# Optional
LLM_MODEL_NAME=llama-3.1-8b-instant
```

---

# Running the Project

## Interactive Command Line

```bash
python app.py
```

---

## Run with a Claim

```bash
python app.py --claim "My home flooded during monsoon; walls need repair under Bharat Griha Raksha."
```

---

## Generate Sample Insurance Documents

```bash
python app.py --generate-pdfs
```

---

## Build the Vector Database

```bash
python app.py --ingest
```

---

## Launch Streamlit Dashboard

```bash
python app.py --ui
```

---

# First-Time Execution

On the first run, the application will automatically:

- Generate sample insurance PDFs (if they do not exist)
- Create document embeddings
- Build the Chroma vector database
- Load the retrieval pipeline

Subsequent runs will reuse the existing vector database, resulting in much faster startup.

---

# System Architecture

```text
                          User Claim
                               │
                               ▼
                    Retrieve Relevant Context
                               │
                               ▼
                     Relevance Grading Agent
                  ┌────────────┴────────────┐
                  │                         │
            Relevant                  Not Relevant
                  │                         │
                  ▼                         ▼
       Claim Adjudication          Query Rewriter
                  │                         │
                  ▼                         ▼
      Hallucination Detection      Retrieve Again
                  │                         │
                  ▼                         ▼
         Confidence Evaluation      Retry Limit Reached?
                  │                         │
          ┌───────┴────────┐         ┌──────┴──────┐
          │                │         │             │
      High Confidence   Low Confidence      Tavily Search
          │                │                 │
          ▼                ▼                 ▼
     Final Decision   Human Escalation  Claim Adjudication
```

---

# Running Tests

```bash
python tests/test_rag_adjudication.py
```

```bash
python tests/test_nodes_pipeline.py
```

Ensure the PDFs have been generated and the vector database has been created before running the tests.

---

# Technologies Used

- Python 3.12
- LangGraph
- LangChain
- Groq LLM
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers
- Streamlit
- Tavily Search
- Pydantic
- ReportLab

---

# Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| GROQ_API_KEY | ✅ | Groq LLM API Key |
| TAVILY_API_KEY | ✅ | Tavily Search API Key |
| LLM_MODEL_NAME | Optional | Override the default Groq model |

---

# Notes

- API keys are loaded from the `.env` file.
- Never commit your `.env` file to GitHub.
- The `vector_db` directory is automatically created after ingestion.
- The project uses the **all-MiniLM-L6-v2** embedding model.
- The default Groq model can be changed using `LLM_MODEL_NAME`.

---

# Git Ignore

The following files and folders should **not** be committed:

```text
.venv/
.env
__pycache__/
vector_db/
*.pyc
.vscode/
.idea/
```

---

# License

This project is developed for educational and research purposes.
