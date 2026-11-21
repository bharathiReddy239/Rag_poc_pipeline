# Local PDF RAG Assistant (Ollama + FAISS + LangChain)

A fully local **Retrieval-Augmented Generation (RAG)** application that lets you ingest multiple PDF documents, index them locally with FAISS, and chat with your documents using Ollama—complete with source filename and page number citations.

---

## Features
- **100% Local & Private:** Uses local Ollama models (`nomic-embed-text` for embeddings and `llama3.2` for generation)—no external API keys or cloud uploads required.
- **Multi-PDF Support:** Automatically scans and indexes all `.pdf` files inside the `data/` directory.
- **Source Citations:** Displays exact PDF filenames and page numbers alongside every generated answer.
- **Interactive Web UI:** Includes a Streamlit chat interface with sidebar PDF upload and one-click index rebuilding.
- **Modular Architecture:** Separated configuration, ingestion, retrieval/generation pipeline, and automated query tests.

---

## Project Structure

```text
PDF_FAISS_RAG_POC/
├── app.py                         # Streamlit web chat interface & PDF uploader
├── data/                          # Input PDF documents
│   └── sample_rag_poc_handbook.pdf
├── src/                           # Core RAG pipeline modules
│   ├── config.py                  # Centralized paths, chunk settings, and model names
│   ├── ingest.py                  # Loads PDFs, splits text, and saves FAISS index
│   └── rag_pipeline.py            # Retrieves context, generates answers, and extracts citations
├── tests/                         # Automated evaluation scripts
│   └── test_queries.py            # Verifies answer generation and source retrieval
└── vectorstore/                   # Persisted local FAISS index
    └── faiss_index_ollama/
```

---

## Prerequisites

1. **Python 3.10+**
2. **[Ollama](https://ollama.com)** installed and running locally.
3. Pull the required Ollama models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3.2
   ```

---

## Setup & Installation

1. **Activate your virtual environment (Windows PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install langchain langchain-community langchain-ollama langchain-text-splitters faiss-cpu pypdf streamlit
   ```

---

## Usage

### 1. Ingest PDFs (Build Vector Index)
Place your PDFs inside the `data/` folder and run:
```powershell
python src/ingest.py
```

### 2. Launch the Web Chat UI (Recommended)
Start the Streamlit app in your browser:
```powershell
streamlit run app.py
```
- Use the **sidebar** to upload additional PDFs and click **Save & Rebuild Index**.
- Ask questions in the chat bar to receive grounded answers with page citations.

### 3. Run via Terminal (CLI Mode)
To query your documents directly in the terminal:
```powershell
python src/rag_pipeline.py
```

### 4. Run Automated Tests
Verify that retrieval and generation are working properly:
```powershell
python tests/test_queries.py
```

---

## Configuration

You can customize chunk sizes, file paths, or Ollama models in `src/config.py`:
- `EMBED_MODEL`: `"nomic-embed-text"`
- `LLM_MODEL`: `"llama3.2"`
- `CHUNK_SIZE`: `500`
- `CHUNK_OVERLAP`: `50`
