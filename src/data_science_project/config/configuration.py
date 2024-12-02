from src.data_science_project.entity.data_ingestion_entity import DataIngestionConfig
from config import *
from src.data_science_project.utils.common import *
from src.data_science_project.constants import *



class ConfigurationManager:

    def __init__(self,config_filepath=CONFIG_FILE_PATH):
        self.config=read_yaml(config_filepath)
        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        print(config.root_dir)
        create_dir([config.root_dir])
        

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config



obj1=ConfigurationManager()
obj1.get_data_ingestion_config()