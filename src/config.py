from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
PDF_PATH = DATA_DIR / "sample_rag_poc_handbook.pdf"
INDEX_PATH = ROOT_DIR / "vectorstore" / "faiss_index_ollama"

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
