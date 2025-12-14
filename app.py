import streamlit as st
from rag_pipeline import get_rag_chain

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("📚 RAG Chatbot")

user_level = st.selectbox(
    "Select your experience level",
    ["beginner", "intermediate", "advanced"]
)

question = st.text_input("Ask a question from the document")

if question:
    with st.spinner("Thinking..."):
        chain = get_rag_chain(user_level)
        answer = chain.invoke(question)
        st.markdown("### Answer")
        st.write(answer)
