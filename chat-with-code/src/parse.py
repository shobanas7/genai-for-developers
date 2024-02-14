import requests
import nbformat
import json
from google.cloud import aiplatform
import vertexai
from vertexai.language_models import CodeGenerationModel
from langchain.schema import HumanMessage, SystemMessage
from langchain.schema.document import Document


vertexai.init(project='genai-cicd', location='us-central1')

# Extracts the python code from an .ipynb file from github


def extract_python_code_from_ipynb(github_url, cell_type="code"):
    raw_url = github_url.replace(
        "github.com", "raw.githubusercontent.com").replace("/blob/", "/")

    response = requests.get(raw_url)
    response.raise_for_status()  # Check for any request errors

    notebook_content = response.text

    notebook = nbformat.reads(notebook_content, as_version=nbformat.NO_CONVERT)

    python_code = None

    for cell in notebook.cells:
        if cell.cell_type == cell_type:
          if not python_code:
            python_code = cell.source
          else:
            python_code += "\n" + cell.source

    return python_code

# Extracts the python code from an .py file from github


def extract_python_code_from_py(github_url):
    raw_url = github_url.replace(
        "github.com", "raw.githubusercontent.com").replace("/blob/", "/")

    response = requests.get(raw_url)
    response.raise_for_status()  # Check for any request errors

    python_code = response.text

    return python_code


def parse_code_from_urls():
    code_strings = []
    with open('code_files_urls.txt') as f:
        code_files_urls = f.read().splitlines()

    for i in range(0, len(code_files_urls)):
        if code_files_urls[i].endswith(".ipynb"):
            content = extract_python_code_from_ipynb(
                code_files_urls[i], "code")
            doc = Document(page_content=content, metadata={
                           "url": code_files_urls[i], "file_index": i})
            code_strings.append(doc)

    return code_strings

