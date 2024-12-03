from src.data_science_project.entity.config_entity import DataValidationConfig
from src.data_science_project import Logger
import pandas as pd


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config
        print(self.config.all_schema)
        

    def validate_all_columns(self):
        try:
            print(self.config.unzip_data_file)
            data=pd.read_csv(self.config.unzip_data_file)
            cols=list(data.columns)
            schema=self.config.all_schema.COLUMNS.keys()
            status=None
            for col in cols:
                if col in list(schema):
                    status=True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation Status: {status}")
                else:
                    status=False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {status}")

            Logger.info("Validation Status has been updated....")


        except Exception as e:
            raise e
        