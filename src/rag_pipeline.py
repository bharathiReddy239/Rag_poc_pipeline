import os
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaEmbeddings
from config import INDEX_PATH, EMBED_MODEL, LLM_MODEL

def ask_rag(question: str):
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    vectorstore = FAISS.load_local(
        str(INDEX_PATH), embeddings, allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 1. Retrieve relevant chunks
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)

    # 2. Extract unique source filenames and page numbers
    sources = sorted({
        f"{os.path.basename(d.metadata.get('source', 'Unknown'))} (Page {d.metadata.get('page', 0) + 1})"
        for d in docs
    })

    # 3. Generate answer
    prompt = ChatPromptTemplate.from_template(
        """Answer based ONLY on the context below. If unknown, say "Not found in document."

Context:
{context}

Question: {question}"""
    )
    llm = ChatOllama(model=LLM_MODEL, temperature=0)
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})

    return {"answer": answer, "sources": sources}

if __name__ == "__main__":
    while (q := input("\nAsk (or 'exit'): ").strip()).lower() != "exit":
        result = ask_rag(q)
        print(f"\nAnswer:\n{result['answer']}")
        print(f"Sources: {', '.join(result['sources'])}")
