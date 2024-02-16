from langchain_community.vectorstores import FAISS

def create_and_store(texts, embeddings):
    db = FAISS.from_documents(texts, embeddings)
    return db