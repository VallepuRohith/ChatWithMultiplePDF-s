import streamlit as st
from dotenv import load_dotenv

from src.pdf_loader import load_pdfs
from src.text_splitter import split_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.qa_chain import get_qa_chain

load_dotenv()

st.set_page_config(page_title="Chat with Multiple PDFs")
st.title("📄 Chat with Multiple PDFs")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    documents = load_pdfs(uploaded_files)
    chunks = split_text(documents)
    embeddings = get_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    qa_chain = get_qa_chain(vector_store)

    query = st.text_input("Ask a question")

    if query:
        result = qa_chain(query)

        st.subheader("Answer")
        st.write(result["result"])

        st.subheader("Sources")
        for doc in result["source_documents"]:
            st.write(
                f"- {doc.metadata.get('source', 'PDF')} | Page {doc.metadata.get('page', 'N/A')}"
            )
