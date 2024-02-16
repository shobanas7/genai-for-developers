# Collect from Github
import requests
import time

# Crawls a GitHub repository and returns a list of files in the repository


# @param {type:"string"}
GITHUB_TOKEN = ""


def crawl_github_repo(url, is_sub_dir, access_token=f"{GITHUB_TOKEN}"):

    ignore_list = ['__init__.py']

    if not is_sub_dir:
        api_url = f"https://api.github.com/repos/{url}/contents"
    else:
        api_url = url

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Check for any request errors

    files = []

    contents = response.json()

    for item in contents:
        if item['type'] == 'file' and item['name'] not in ignore_list and (item['name'].endswith('.py') or item['name'].endswith('.ipynb')):
            files.append(item['html_url'])
        elif item['type'] == 'dir' and not item['name'].startswith("."):
            sub_files = crawl_github_repo(item['url'], True)
            time.sleep(.1)
            files.extend(sub_files)

    return files


def collect_files_urls(repo):
  code_files_urls = crawl_github_repo(repo, False, GITHUB_TOKEN)

  # Write list to a file so you do not have to download each time
  with open('code_files_urls.txt', 'w') as f:
      for item in code_files_urls:
          f.write(item + '\n')


def filter_file_urls(type=None):
    urls = []
    with open('code_files_urls.txt') as f:
        code_files_urls = f.read().splitlines()

    for i in range(0, len(code_files_urls)):
        if type != None:
            if code_files_urls[i].endswith("." + type):
                urls.append(code_files_urls[i])
                
        else:
            urls.append(code_files_urls[i])
        
    return urls

def urls_from_type(repo, type):
    collect_files_urls(repo)
    return filter_file_urls(type)
