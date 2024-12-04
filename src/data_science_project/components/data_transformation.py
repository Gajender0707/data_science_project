from src.data_science_project.entity.config_entity import DataTransformationConfig
from src.data_science_project.utils.common import *
from sklearn.model_selection import train_test_split
from src.data_science_project.config.configuration import ConfigurationManager
import pandas as pd
from pathlib import Path
import os
from src.data_science_project import Logger



class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        
    def data_splitting(self):
        try:
            data=pd.read_csv(self.config.data_path)

            #splitting the data into the train and test portion.....
            train_data,test_data=train_test_split(data,random_state=42)
 
            create_dir([self.config.root_dir])
            
            # ## Saving the data into the Train and test Poration after doing the all type of Feature Engineering 
            # ## and the EDA Part in this portion......

            train_data.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
            test_data.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

            Logger.info(f"Data has been splitted into the Train and test and saved to {self.config.root_dir}.")
            Logger.info(f"Training Data shpae: {train_data.shape}")
            Logger.info(f"Testing Data shape: {test_data.shape}")

        except Exception as e:
            raise e






# if __name__=="__main__":
#     config=ConfigurationManager()
#     data_transforamtion_config=config.get_data_transfomation_config()
#     obj=DataTransformation(config=data_transforamtion_config)
#     obj.data_splitting()
    
