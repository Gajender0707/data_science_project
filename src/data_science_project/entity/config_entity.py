from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_file: Path
    STATUS_FILE: str
    all_schema:dict



@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    STATUS_FILE: str


@dataclass 
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


@dataclass
class ModelEvalutionConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_path: Path
    all_params: dict
    target_column: str
    mlflow_tracking_uri: str
    mlflow_tracking_username: str
    mlflow_tracking_password: str