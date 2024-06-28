from langchain.document_loaders.pdf import PyPDFDirectoryLoader
def load_documents():
    document_loader = PyPDFDirectoryLoader("data")
    return document_loader.load()

# Call the function to load documents
documents = load_documents()
print(documents)
