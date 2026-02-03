from langchain.document_loaders import PyPDFLoader
import tempfile

def load_pdfs(uploaded_files):
    documents = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.read())
            loader = PyPDFLoader(tmp.name)
            documents.extend(loader.load())
    return documents
