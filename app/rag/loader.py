from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
import pandas as pd


def load_pdf(path: str):
    loader = PyPDFLoader(path)
    return loader.load()


def load_csv(path: str):
    df = pd.read_csv(path)
    documents = []

    for _, row in df.iterrows():
        content = f"Question: {row['question']}\nAnswer: {row['answer']}"
        documents.append(
            Document(
                page_content=content,
                metadata={"source": "faq.csv"}
            )
        )

    return documents


def load_all_documents(pdf_path: str, csv_path: str):
    return load_pdf(pdf_path) + load_csv(csv_path)
