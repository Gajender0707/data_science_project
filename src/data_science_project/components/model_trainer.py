from src.data_science_project.entity.config_entity import ModelTrainerConfig
from src.data_science_project.utils.common import *
from src.data_science_project.config.configuration import ConfigurationManager
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
import pandas as pd

class ModelTrainer:

    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def train(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path)
            X=train_data.drop(self.config.target_column,axis=1)
            y=train_data[self.config.target_column]
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
            print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
            ls=ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio)
            ls.fit(X_train,y_train)
            save_model(ls,os.path.join(self.config.root_dir,self.config.model_name))


        except Exception as e:
            raise e




# if __name__=="__main__":
#     config=ConfigurationManager()
#     model_trainer_config=config.get_model_trainer_config()
#     obj=ModelTrainer(config=model_trainer_config)
#     obj.train()