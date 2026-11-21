import sys
from pathlib import Path
import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent / "src"))
from config import DATA_DIR
from ingest import build_index
from rag_pipeline import ask_rag

st.set_page_config(page_title="PDF RAG Assistant", layout="centered")
st.title("Local PDF RAG Assistant (Ollama + FAISS)")

# Sidebar: Upload & Re-index PDFs
with st.sidebar:
    st.header("Document Management")
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    if st.button("Save & Rebuild Index") and uploaded_files:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        for file in uploaded_files:
            (DATA_DIR / file.name).write_bytes(file.getvalue())
        with st.spinner("Indexing PDFs..."):
            build_index()
        st.success("Index updated!")

# Main Chat Interface
if prompt := st.chat_input("Ask a question about your PDFs..."):
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            result = ask_rag(prompt)
            st.write(result["answer"])
            st.caption(f"Sources: {', '.join(result['sources'])}")
