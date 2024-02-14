# Chunk code strings
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_code(code_strings):
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    texts = text_splitter.split_documents(code_strings)
    return texts



