from src.data_science_project import Logger
from pathlib import Path
from src.data_science_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.data_science_project.pipeline.data_validation_pipeline import DataValidationPipeline
from src.data_science_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.data_science_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.data_science_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline





STAGE_NAME="Data Ingestion Pipeline"
try:
    Logger.info(f"<<<<<<<<<<<<{STAGE_NAME} has been started....>>>>>>>>>>>>>>>>")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    Logger.info(f"<<<<<<<<<<<<{STAGE_NAME} has been Completed.....>>>>>>>>>>>>>>>")

except Exception as e:
    raise e






STAGE_NAME="Data Validation Pipeline"
try:
    Logger.info(f"<<<<<<<<<<<<{STAGE_NAME} has been started....>>>>>>>>>>>>>>>>")
    data_validation_pipeline=DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()
    Logger.info(f"<<<<<<<<<<<<<<{STAGE_NAME} has been Completed......>>>>>>>>>>>>>>")

except Exception as e:
    raise e







STAGE_NAME="Data Transformation Pipeline"
try:
    Logger.info(f"<<<<<<<<{STAGE_NAME} has been started>>>>>>>>>>>>>>")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    Logger.info(f"<<<<<<<<<<<<<<<<{STAGE_NAME} has been Completed......>>>>>>>>>>>>>>")

except Exception as e:
    raise e







STAGE_NAME="Model Trainer Pipeline"
try:
    Logger.info(f"<<<<<<<<{STAGE_NAME} has been started>>>>>>>>>>>>>>")
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    Logger.info(f"<<<<<<<<<<<<<<<<{STAGE_NAME} has been Completed......>>>>>>>>>>>>>>")

except Exception as e:
    raise e







STAGE_NAME="Model Evaluation Pipeline"
try:
    Logger.info(f"<<<<<<<<{STAGE_NAME} has been started>>>>>>>>>>>>>>")
    model_evaluation_pipeline=ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evalution()
    Logger.info(f"<<<<<<<<<<<<<<<<{STAGE_NAME} has been Completed......>>>>>>>>>>>>>>")

except Exception as e:
    raise e









