from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

BASE_DIR = Path(__file__).parent

VECTORSTORE_PATH = BASE_DIR / "vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=str(VECTORSTORE_PATH),
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})

question = input("Ask a question: ")

docs = retriever.invoke(question)

print("\nResults:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)
    print(doc.page_content)
    print()