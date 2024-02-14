
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA



prompt_zero_shot = """
    You are a proficient python developer. Respond with the syntactically 
    correct & concise code for to the question below.

    Question:
    {question}

    Output Code :
    """

prompt_prompt_zero_shot = PromptTemplate(
  input_variables=["question"],
  template=prompt_zero_shot,
)

# RAG template
prompt_RAG = """
    You are a proficient python developer. Respond with the syntactically correct code for to the question below. Make sure you follow these rules:
    1. Use context to understand the APIs and how to use it & apply.
    2. Do not add license information to the output code.
    3. Do not include colab code in the output.
    4. Ensure all the requirements in the question are met.

    Question:
    {question}

    Context:
    {context}

    Helpful Response :
    """

def rag_prompt():
    prompt_RAG_tempate = PromptTemplate(
        template=prompt_RAG, input_variables=["context", "question"]
    )
    return prompt_RAG_tempate