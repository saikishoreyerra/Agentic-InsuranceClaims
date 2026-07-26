import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config.settings import DATA_DIR, VECTOR_DB_DIR, EMBEDDING_MODEL_NAME


def run_ingestion():
    """Load policy PDFs, chunk them, and persist embeddings to Chroma."""
    data_dir = str(DATA_DIR)
    print(f"📥 [Ingest] Reading PDFs from: {data_dir}")
    print(f"💾 [Ingest] Target Vector DB path: {VECTOR_DB_DIR}")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        print("⚠️ Data directory created.")

    # recursive=True required: PDFs live under data/policies|endorsements|regulations
    loader = PyPDFDirectoryLoader(data_dir, recursive=True)
    docs = loader.load()

    if not docs:
        print("⚠️ No PDF files found in data directory!")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    print(f"✂️ Split {len(docs)} documents into {len(chunks)} chunks.")

    # Using lightweight MiniLM embedding model
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )
    print("✅ Ingestion complete! Vector store successfully generated.")


if __name__ == "__main__":
    run_ingestion()
