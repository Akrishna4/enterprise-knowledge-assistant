# Enterprise Knowledge Assistant (RAG-based Chatbot)

## Overview

The **Enterprise Knowledge Assistant** is a Retrieval-Augmented Generation (RAG) based chatbot that enables interns and employees to query internal company documents using natural language.

Instead of manually searching through policy PDFs or FAQ files, users can ask questions in a chat interface and receive accurate, context-aware answers grounded strictly in the organization’s internal documents.

This project was built as part of an **AI/ML Internship Assessment** to demonstrate practical understanding of LLMs, RAG pipelines, backend APIs, and lightweight UI development.

---

## Problem Statement

In most organizations, important information such as internship policies, leave rules, working hours, onboarding requirements, and exit procedures are stored in static documents. This often leads to:

* Time wasted searching through PDFs
* Repetitive queries to HR or managers
* Inconsistent or delayed responses

The goal of this project is to **simplify access to internal knowledge** by providing a conversational chatbot that answers questions directly from official company documents.

---

## Solution Approach

This project uses a **Retrieval-Augmented Generation (RAG)** architecture:

* Documents are first indexed and converted into embeddings
* When a question is asked, only the most relevant document chunks are retrieved
* The LLM generates answers **only using retrieved context**

This approach ensures:

* Reduced hallucinations
* High factual accuracy
* Answers remain aligned with company policies

---

## Architecture (RAG Flow)

```
User (Streamlit Chat UI)
        ↓
FastAPI Backend (app/main.py)
        ↓
Document Loader (PDF + CSV)
        ↓
Text Chunking
        ↓
Embedding Generation (HuggingFace)
        ↓
Vector Retrieval (Semantic Search)
        ↓
LLM Answer Generation (Groq)
        ↓
Answer returned to UI
```

---

## Tech Stack

### Programming Language

* Python

### Backend

* FastAPI – REST API for question answering
* LangChain – RAG pipeline orchestration

### AI / ML

* HuggingFace sentence-transformer models (embeddings)
* Groq LLM API (answer generation)
* Retrieval-Augmented Generation (RAG)

### Frontend

* Streamlit – chat-based UI

### Data Sources

* Company policy PDF
* FAQ CSV file

---

## AI & Cloud Services Used

* **Groq API** – LLM inference
* **HuggingFace Models** – text embeddings
* **Local Vector Store** – semantic document retrieval

(No managed cloud database was required; focus was on correctness of the RAG implementation.)

---

## How AI Helped Reduce Manual Effort

* Eliminated the need to manually search policy documents
* Reduced dependency on HR for common queries
* Enabled instant and consistent responses
* Improved accessibility of internal knowledge

---

## Project Structure

```
enterprise-knowledge-assistant/
├── app/
│   ├── rag/
│   │   ├── loader.py
│   │   ├── embedder.py
│   │   ├── retriever.py
│   │   └── chain.py
│   └── main.py
├── data/
│   ├── company_policy.pdf
│   └── faq.csv
├── chat_ui.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Akrishna4/enterprise-knowledge-assistant.git
cd enterprise-knowledge-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file using `.env.example`:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run Backend

```bash
uvicorn app.main:app --reload
```

### 6. Run Chat UI

```bash
streamlit run chat_ui.py
```

---

## Example Questions Supported

* How long is the internship duration?
* How many leaves are interns allowed per month?
* Is work from home allowed?
* What are the working hours?
* What documents are required during onboarding?
* What is the notice period for interns?

---

## Challenges & Learnings

### Challenges

* Managing LangChain dependency compatibility
* Designing a clean RAG pipeline without hallucinations
* Handling Git and project structure correctly
* Balancing simplicity and functionality in the UI

### Key Learnings

* Practical understanding of RAG architecture
* Hands-on experience with LLM APIs
* Importance of document-grounded answers
* Clean repository and secret management practices

---

## Project Explanation Video

📹 **Video Explanation Link:**
https://drive.google.com/file/d/154_4wjEYe5TvlpmWUHENcpZSuFc2KpkK/view?usp=drive_link

The video covers:

* Project idea and motivation
* RAG architecture walkthrough
* AI and cloud services used
* Key challenges and learnings

---

## Submission Notes

* Complete source code is included
* No API keys or secrets are exposed
* Repository follows best practices
* Designed for easy review and execution

---

## Author

**Ayush Krishna**
B.Tech (Electronics & Computer Engineering)
LinkedIn: [https://www.linkedin.com/in/ayush-krishna-b5b149304/](https://www.linkedin.com/in/ayush-krishna-b5b149304/)

---

