# Based on 
# https://medium.com/@rubenszimbres/code-generation-using-retrieval-augmented-generation-langchain-861e3c1a1a53

from utils.collect import github
from utils.parse import ipynb
from utils.chunk import code
from utils.embedding import vertex
from utils.store import faiss
from utils import collect
import search, load_from, prompts


from langchain_google_vertexai import VertexAI
from langchain.chains import RetrievalQA



# GITHUB_REPO = "GoogleCloudPlatform/bank-of-anthos"
GITHUB_REPO = "GoogleCloudPlatform/generative-ai"
db = load_from.ingest_code_from_repo(GITHUB_REPO, type="ipynb")


# ## SEARCH
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
non_rag_response = code_llm.invoke(
    input=user_question, max_output_tokens=2048, temperature=0.1)
print(non_rag_response)
print()



####
print("Model with RAG")

qa_chain = RetrievalQA.from_llm(
    llm=code_llm, prompt=prompts.rag_prompt(), retriever=retriever, return_source_documents=True
)

results = qa_chain.invoke({"query": user_question})  # ✅
print(results["result"])

