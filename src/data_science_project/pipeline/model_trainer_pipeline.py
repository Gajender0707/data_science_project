from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.model_trainer import ModelTrainer
from src.data_science_project import Logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        Logger.info("Model Has been Train Successfully...")