from langchain.embeddings import VertexAIEmbeddings

def get_embedding():
    EMBEDDING_QPM = 100
    EMBEDDING_NUM_BATCH = 5
    embeddings = VertexAIEmbeddings(
        requests_per_minute=EMBEDDING_QPM,
        num_instances_per_batch=EMBEDDING_NUM_BATCH,
        model_name = "textembedding-gecko@latest"
    )
    return embeddings