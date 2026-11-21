from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DATA_DIR, INDEX_PATH, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

def build_index():
    print(f"Scanning all PDFs in: {DATA_DIR}")
    loader = PyPDFDirectoryLoader(str(DATA_DIR))
    docs = loader.load()

    if not docs:
        raise ValueError(f"No PDFs found in {DATA_DIR}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(INDEX_PATH))
    print(f"Indexed {len(chunks)} chunks from {len(docs)} pages -> {INDEX_PATH}")

if __name__ == "__main__":
    build_index()
