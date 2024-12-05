from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.model_evaluation import ModelEvaluation
from src.data_science_project import Logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evalution(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_mlflow_tracking()
        Logger.info("Model Evaluation Pipeline Defined Sucessfully....")