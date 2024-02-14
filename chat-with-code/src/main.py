# Based on 
# https://medium.com/@rubenszimbres/code-generation-using-retrieval-augmented-generation-langchain-861e3c1a1a53

import collect, parse, chunk, embedding, index, search, prompts
from langchain.llms import VertexAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
## COLLECT
#collect.write_code_files_urls()

## PARSE
code_strings=parse.parse_code_from_urls()

## CHUNK
code_chunks = chunk.chunk_code(code_strings)

## EMBEDING
embeddings = embedding.get_embedding()

## STORE INDEX
db = index.create_and_store_index(code_chunks, embeddings)

## SEARCH
retriever = search.get_similarity_retriever(db)

## RUN
code_llm = VertexAI(
    model_name="code-bison",
    max_output_tokens=2048,
    temperature=0.1,
    verbose=False,
    )


user_question = """what does the print_autosxs_judgments method do. 
if you don't know say i don't know"""

print("Model without RAG")
non_rag_response = code_llm.predict(text=user_question, max_output_tokens=2048, temperature=0.1)
print(non_rag_response)
print()



####
print("Model with RAG")

qa_chain = RetrievalQA.from_llm(
    llm=code_llm, prompt=prompts.rag_prompt(), retriever=retriever, return_source_documents=True
)

results = qa_chain({"query": user_question})  # ✅
print(results["result"])
