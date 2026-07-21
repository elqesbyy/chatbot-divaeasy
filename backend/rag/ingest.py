from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).parent

DOCUMENTS_PATH = BASE_DIR / "documents"
VECTORSTORE_PATH = BASE_DIR / "vectorstore"


# -----------------------------
# Load Markdown files
# -----------------------------
documents = []

for file in DOCUMENTS_PATH.glob("*.md"):
    print(f"Loading: {file.name}")

    loader = TextLoader(
        str(file),
        encoding="utf-8"
    )

    documents.extend(loader.load())


print(f"\nLoaded {len(documents)} document(s).")


# -----------------------------
# Split into chunks
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")


# -----------------------------
# Embedding model
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Create Chroma database
# -----------------------------
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(VECTORSTORE_PATH)
)

print("\nVector database created successfully!")

print(f"Saved in: {VECTORSTORE_PATH}")