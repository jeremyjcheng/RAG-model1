from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents():
    document_loader = PyPDFDirectoryLoader("./")
    documents = document_loader.load()
    print("Documents loaded:", documents)  # Debug print
    return documents

# Call the function to load documents
documents = load_documents()
print("Final documents output:", documents)
