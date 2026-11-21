import sys
from pathlib import Path

# Link to src/ folder so we can import ask_rag
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
from rag_pipeline import ask_rag

TEST_QUESTIONS = [
    "What is the main topic of this handbook?",
    "Summarize the key guidelines mentioned in the document.",
]

def run_tests():
    print("Running automated RAG tests...\n")
    for idx, q in enumerate(TEST_QUESTIONS, 1):
        result = ask_rag(q)
        assert result["answer"], f"Test {idx} failed: Empty answer"
        assert len(result["sources"]) > 0, f"Test {idx} failed: No sources returned"
        print(f"[PASS] Q{idx}: {q}")
        print(f"       Answer: {result['answer'][:100]}...")
        print(f"       Sources: {result['sources']}\n")

if __name__ == "__main__":
    run_tests()
