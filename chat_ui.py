import streamlit as st
import requests

# =============================
# Configuration
# =============================
API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    layout="centered"
)

# =============================
# Custom CSS (clean, enterprise)
# =============================
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* Hero */
.hero {
    background: white;
    padding: 2.5rem 2rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    text-align: center;
    margin-bottom: 2rem;
}

.hero h1 {
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.hero p {
    color: #6b7280;
    font-size: 1rem;
}

/* Suggestions */
.suggestions {
    background: white;
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #eef0f4;
    margin-bottom: 2rem;
}

/* Chat bubbles */
.stChatMessage.user {
    background-color: #e8f0fe;
    border-radius: 14px;
    padding: 12px;
}

.stChatMessage.assistant {
    background-color: #ffffff;
    border-radius: 14px;
    padding: 12px;
    border: 1px solid #eef0f4;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Hero Section
# =============================
st.markdown("""
<div class="hero">
    <h1>💬 Enterprise Knowledge Assistant</h1>
    <p>Ask questions from internal company documents</p>
</div>
""", unsafe_allow_html=True)

# =============================
# Session State
# =============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =============================
# Helper: Ask Question
# =============================
def ask_question(question: str):
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=60
            )
            if response.status_code == 200:
                answer = response.json().get("answer", "")
            else:
                answer = "Something went wrong while fetching the answer."
        except Exception as e:
            answer = f"Error: {e}"

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# =============================
# Suggested Questions (UX-CURATED)
# =============================
primary_questions = [
    "How long is the internship duration?",
    "What are the working hours for interns?",
    "How many leaves are interns allowed per month?",
    "Is work from home allowed for interns?",
    "What documents are required during onboarding?",
    "What is the notice period for interns?"
]

additional_questions = [
    "Does completing the internship guarantee a full-time job?",
    "Is internship extension allowed?",
    "Is attendance monitored for interns?",
    "Can unused leaves be carried forward?",
    "Are interns paid a stipend?",
    "How is the stipend paid?",
    "What happens if an intern violates company policies?",
    "Are interns required to maintain confidentiality?",
    "Can interns raise grievances?",
    "Is an internship completion certificate provided?"
]

st.markdown('<div class="suggestions">', unsafe_allow_html=True)
st.markdown("#### 💡 Suggested questions")

cols = st.columns(2)
for i, q in enumerate(primary_questions):
    if cols[i % 2].button(q, use_container_width=True, key=f"primary_{i}"):
        ask_question(q)
        st.rerun()

with st.expander("More example questions"):
    for j, q in enumerate(additional_questions):
        if st.button(q, use_container_width=True, key=f"extra_{j}"):
            ask_question(q)
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Chat History
# =============================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =============================
# Chat Input
# =============================
user_query = st.chat_input("Ask a question...")

if user_query:
    ask_question(user_query)
    st.rerun()
