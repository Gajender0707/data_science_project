from src.data_science_project.entity.data_ingestion_entity import *
import urllib.request as request
from src.data_science_project import Logger
from src.data_science_project.utils.common import create_dir
import os
import zipfile

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            request.urlretrieve(self.config.source_url,self.config.local_data_file)
            Logger.info(f"Data has been saved on the file location {self.config.local_data_file}")
        else:
            Logger.info(f"file already Exists....")

    def extract_file(self):
        unzip_path=self.config.unzip_dir
        create_dir([unzip_path])
        with zipfile.ZipFile(self.config.local_data_file,"r") as f:
            f.extractall(unzip_path)

        Logger.info(f"Data has been Extract to location {unzip_path}")





obj1=DataIngestion(DataIngestionConfig)



