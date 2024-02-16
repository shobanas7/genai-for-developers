# Chunk text strings
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_code(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)
    return texts
