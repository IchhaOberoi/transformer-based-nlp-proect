import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "transformer-based-nlp-project"
AUTHOR_USER_NAME = "IchhaOberoi"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ichhaoberoi08@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Transformer Based NLP Project",
    long_description=long_description,  # Fixed field name
    long_description_content_type="text/markdown",  # Fixed field name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)







    