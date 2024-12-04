from src.data_science_project.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                           DataTransformationConfig,
                                                           ModelTrainerConfig)
from config import *
from src.data_science_project.utils.common import *
from src.data_science_project.constants import *



class ConfigurationManager:

    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH,
                 params_filepath=PARAM_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.schema=read_yaml(schema_filepath)
        self.params=read_yaml(params_filepath)
        create_dir([self.config.artifacts_root])


    ## Function for getting the Configuration details for data ingestion part...
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
    



    ## Function for the getting the configuration details of data validation...
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_file=config.unzip_data_file,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=self.schema
        )
        return data_validation_config
    


     ## Function for the getting the configuration details of data Transformation...
    def get_data_transfomation_config(self) -> DataTransformationConfig:
        config=self.config.data_transformation

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            STATUS_FILE=config.STATUS_FILE)
        return data_transformation_config




     ## Function for the getting the configuration details of model trainer...
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config=self.config.model_trainer
        params=self.params.Elastic_net
        schema=self.schema.TARGET_COLUMN
        create_dir([config.root_dir])

        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )
        return model_trainer_config
    








# if __name__=="__main__":
#     obj=ConfigurationManager()
#     model_trainer_details=obj.get_model_trainer_config()
#     print(model_trainer_details)
        
        
    



    





