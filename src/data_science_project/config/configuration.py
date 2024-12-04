from src.data_science_project.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                           DataTransformationConfig)
from config import *
from src.data_science_project.utils.common import *
from src.data_science_project.constants import *



class ConfigurationManager:

    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.schema=read_yaml(schema_filepath)
        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        create_dir([config.root_dir])
        

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_file=config.unzip_data_file,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=self.schema
        )

        return data_validation_config
    

    def get_data_transfomation_config(self) -> DataTransformationConfig:
        config=self.config.data_transformation

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            STATUS_FILE=config.STATUS_FILE)
        return data_transformation_config




# if __name__=="__main__":
#     obj=ConfigurationManager()
#     obj.get_data_transfomation_config()
        
        
    



    





