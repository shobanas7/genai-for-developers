#https://python.langchain.com/docs/use_cases/question_answering/quickstart
# pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai chromadb bs4


from langchain_community.document_loaders import WebBaseLoader



def from_web(url):
    # Load & Parse
    loader = WebBaseLoader(
        web_paths=(url),
    )
    return loader.load()
