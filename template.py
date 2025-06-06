import os
import pathlib
from pathlib import Path
import logging
import sys

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'mlflow_project'

file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for fpath in file_list:
    fpath = Path(fpath)
    filedir, filename = os.path.split(fpath)
    
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} - for {filename}")
        
    if (not os.path.exists(fpath)) or (os.path.getsize(fpath) == 0):
        with open(fpath, 'w') as f:
            pass
        logging.info(f"Creating empty file - {fpath}")
        
    else:
        logging.info(f"Oops! The {filename} already exists ")