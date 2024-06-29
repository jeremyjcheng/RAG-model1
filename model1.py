from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.embeddings import BedrockEmbeddings

def load_documents():
    document_loader = PyPDFDirectoryLoader("./")
    documents = document_loader.load()
    #print("Documents loaded:", documents)  # Debug print
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 50, length_function= len, is_separator_regex= False)
    return text_splitter.split_documents(documents)

def embedding_function():
    embeddings = BedrockEmbeddings(region_name= "us-east-1", credentials_profile_name= "", model_id= "")