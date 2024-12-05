from src.data_science_project.entity.config_entity import ModelEvalutionConfig
from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.utils.common import *
import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow.sklearn
import numpy as np
import os
import pandas as pd


class ModelEvaluation:
    def __init__(self,config:ModelEvalutionConfig):
        self.config=config


    def eval_metrics(self,actual,pred):
        mse=mean_squared_error(actual,pred)
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)

        return mse,mae,r2

    def log_mlflow_tracking(self):
        os.environ["MLFLOW_TRACKING_URI"]=self.config.mlflow_tracking_uri
        os.environ["MLFLOW_TRACKING_USERNAME"]=self.config.mlflow_tracking_username
        os.environ["MLFLOW_TRACKING_PASSWORD"]=self.config.mlflow_tracking_password
        create_dir([self.config.root_dir])

        with mlflow.start_run():
            test_data=pd.read_csv(self.config.test_data_path)
            test_data_x=test_data.drop(self.config.target_column,axis=1)
            test_data_y=test_data[self.config.target_column]
            model=load(self.config.model_path)
            y_pred=model.predict(test_data_x)

            mse,mae,r2=self.eval_metrics(test_data_y,y_pred)
            accuracy=model.score(test_data_x,test_data_y)
            metrics_data={
                "mse":mse,
                "mae":mae,
                "r2_score":r2,
                "accuracy":accuracy
            }

            save_json(Path(self.config.metric_file_path),metrics_data)

            ## Now track the all Metrics with the mlflow....

            mlflow.log_metric("mse",mse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2_score",r2)
            mlflow.log_metric("accuracy",accuracy)

            ##Now the log the Params with mlflow trakcing

            mlflow.log_param("alpha",self.config.all_params.alpha)
            mlflow.log_param("alpha",self.config.all_params.alpha)


            ## Now log the model with the help of mlflow.skleaern
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="Model",
                registered_model_name="ElasticNetModel"
            )

            Logger.info("Model has been Tracked Sucessfully...")




# if __name__=="__main__":
#     config=ConfigurationManager()
#     model_evaluation_config=config.get_model_evaluation_config()
#     # print(model_evaluation_config)
#     obj=ModelEvaluation(config=model_evaluation_config)
#     obj.log_mlflow_tracking()