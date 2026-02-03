from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os


def load_pdfs(uploaded_files):
    documents = []

    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        documents.extend(loader.load())

        os.remove(tmp_path)

    return documents
