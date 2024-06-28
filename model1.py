from langchain_community.document_loaders import TextLoader

loader = TextLoader("life.pdf")
loader.load()