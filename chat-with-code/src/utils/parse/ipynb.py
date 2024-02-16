import requests
import nbformat

import vertexai


from langchain.schema.document import Document


vertexai.init(project='genai-cicd', location='us-central1')

# Extracts the python code from an .ipynb file from github
def get_code_from_github_url(github_url, cell_type="code"):
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


def from_ipynb(urls):
    code_strings = []

    for i in range(0, len(urls)):
        content = get_code_from_github_url(
            urls[i], "code")
        doc = Document(page_content=content, metadata={
                        "url": urls[i], "file_index": i})
        code_strings.append(doc)

    return code_strings


def from_urls(type, urls):
    if type == "ipynb":
        return from_ipynb(urls)
