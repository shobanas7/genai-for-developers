# Chunk code strings
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_chunked_python(code_strings):
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    texts = text_splitter.split_documents(code_strings)
    return texts


def get_chunked_java(code_strings):
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.Java, chunk_size=2000, chunk_overlap=200
    )
    texts = text_splitter.split_documents(code_strings)
    return texts


def from_type(type, code_strings):
    if type == "python":
        return get_chunked_python(code_strings)
    elif type == "ipynb":
        return get_chunked_python(code_strings)
    elif type == "java":
        return get_chunked_java(code_strings)
    
