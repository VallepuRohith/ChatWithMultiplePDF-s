from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

def get_qa_chain(vector_store):
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True
    )
