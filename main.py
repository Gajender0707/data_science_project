from src.data_science_project import Logger
from pathlib import Path
from src.data_science_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Pipeline"

try:
    Logger.info(f"{STAGE_NAME} has been started....")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    Logger.info(f"{STAGE_NAME} has been Completed......")

except Exception as e:
    raise e







