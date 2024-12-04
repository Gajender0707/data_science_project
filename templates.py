import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


project_name="data_science_project"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion_pipeline.py",
    f"src/{project_name}/pipeline/data_validation_pipeline.py",
    f"src/{project_name}/pipeline/data_transformation_pipeline.py",
    f"src/{project_name}/pipeline/model_trainer_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/common.py",
    ".github/workflows/.gitkeep",
    "templates/index.html",
    "research/research.ipynb",
    "config/config.yaml",
    #files which will in direct main repo: DATA_SCIENCE_PROJECT
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    "params.yaml",
    "schema.yaml",
    "main.py"
]




for filepath in list_of_files:
    filepath=Path(filepath)
    dirname,filename=os.path.split(filepath)

    if dirname!="":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f"{dirname} has been Created Successfully.... ")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"{filename} has been created Successfully....")

    else:
        logging.info(f"{filename} exists already....")
