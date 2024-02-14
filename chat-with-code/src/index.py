from langchain.vectorstores import FAISS

def create_and_store_index(texts, embeddings):
    db = FAISS.from_documents(texts, embeddings)
    return db