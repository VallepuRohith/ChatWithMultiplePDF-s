def get_retriever(vector_store, k=4):
    """
    Creates a retriever for semantic search over the vector database.

    Args:
        vector_store: FAISS vector store
        k (int): Number of relevant chunks to retrieve

    Returns:
        Retriever object
    """
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
