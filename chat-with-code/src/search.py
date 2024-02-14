

def get_similarity_retriever(db):
    # Init your retriever.
    retriever = db.as_retriever(
        search_type="similarity",  # Also test "similarity", "mmr"
        search_kwargs={"k": 5},) 
    return retriever

def get_mmr_retriever(db):
    # Init your retriever.
    retriever = db.as_retriever(
        search_type="mmr",  # Also test "similarity", "mmr"
        search_kwargs={"k": 5},) 
    return retriever

   