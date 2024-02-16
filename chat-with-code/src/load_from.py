from utils import collect, parse, chunk, embedding
import utils.store as db
import utils.parse as parse



# ingest_code_from_repo


def ingest_code_from_repo(repo, type):
    ## COLLECT
    urls = collect.github.urls_from_type(repo=repo, type=type)

    ## PARSE
    code_files = parse.ipynb.from_urls(type=type, urls=urls)

    ## CHUNK
    code_chunks = chunk.code.from_type(type=type, code_strings=code_files)
    
    ## EMBEDING
    engine = embedding.vertex.get_embedding()

    ## STORE INDEX
    return db.faiss.create_and_store(code_chunks, engine)


