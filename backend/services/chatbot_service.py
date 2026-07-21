from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

VECTORSTORE = BASE_DIR / "rag" / "vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=str(VECTORSTORE),
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": 4}
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def ask_chatbot(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are DivaEasy's official AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:

"Je ne trouve pas cette information sur le site de DivaEasy."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content