import setuptools
from urllib.parse import urlparse

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

github_url = "https://github.com/izzad2413/dataset_generator.git" # copy the github repo url
parsed_url = urlparse(github_url)
path_parts = parsed_url.path.strip("/").split("/")

# getting info from url
REPO_NAME = path_parts[1].removesuffix(".git") # copy from github link
AUTHOR_USER_NAME = path_parts[0] # github username
SRC_REPO = REPO_NAME # from template.py project_name
AUTHOR_EMAIL = "author_email"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="description about the project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)