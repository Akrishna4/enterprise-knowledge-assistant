from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from app.rag.loader import load_all_documents
from app.rag.embedder import create_vector_store
from app.rag.retriever import get_retriever
from app.rag.chain import create_rag_chain

load_dotenv(".env")

app = FastAPI(title="Enterprise Knowledge Assistant (Groq + Local Embeddings)")


class Query(BaseModel):
    question: str


# ---- Startup initialization ----
documents = load_all_documents(
    pdf_path="data/company_policy.pdf",
    csv_path="data/faq.csv"
)

vector_store = create_vector_store(documents)
retriever = get_retriever(vector_store)
rag_chain = create_rag_chain(retriever)


@app.post("/ask")
def ask_question(query: Query):
    response = rag_chain.invoke({"query": query.question})
    return {"answer": response["result"]}
