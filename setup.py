import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_desc = f.read()
    
__version__ = '0.0.0'

REPO_NAME = "end-to-end-data-analysis"
AUTHOR_NAME = "rohit-sram"
AUTHOR_EMAIL = 'rohitsram10@outlook.com'
SRC_REPO = "mlflow_project"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='Small Python package for ML use',
    long_description=long_desc,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)