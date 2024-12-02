import os
from pathlib import Path
from ensure import ensure_annotations
import yaml
import zipfile
# from box import ConfigBox
# from attrdict import AttrDict
from dotmap import DotMap
from src.data_science_project import Logger
from box.exceptions import BoxValueError
from dotmap import DotMap


## Function for Reading the data...
@ensure_annotations
def read_yaml(file_path:Path) -> DotMap:
    try:
        with open(file_path,"rb") as yaml_file:
            data=yaml.safe_load(yaml_file)
            Logger.info("Yaml file has been Read Sucessfully....")
        return DotMap(data)
    
    except BoxValueError:
        raise ValueError("Yaml file is empty")

    except Exception as e:
        raise e


## Function for Creating the directory
@ensure_annotations
def create_dir(dirpath_list:list,verbos=True):
    for dirpath in dirpath_list:
        os.makedirs(dirpath,exist_ok=True)
    if verbos:
        Logger.info(f"a Directory has been created on {dirpath} Location...")









