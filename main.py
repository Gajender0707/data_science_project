from src.data_science_project import Logger
from pathlib import Path

from src.data_science_project.utils.common import read_yaml


info=read_yaml(Path("/Users/sanju/Documents/DS/MLOps/data_science_project/params.yaml"))
print(info.name)
print(info.class_name)



