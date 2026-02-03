from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.retriever import get_retriever

def get_qa_chain(vector_store):
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0
    )

    retriever = get_retriever(vector_store)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
