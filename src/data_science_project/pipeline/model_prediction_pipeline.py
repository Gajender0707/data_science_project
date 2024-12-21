from pathlib import Path
from joblib import load
from src.data_science_project.utils.common import read_yaml,load_model

class Prediction:

    def __init__(self):
        model_path=read_yaml(Path("config/config.yaml")).model_evaluation.model_path
        self.model=load_model(Path(model_path))

    def predict(self,data):
        prediction=self.model.predict(data)
        return prediction


if __name__=="__main__":
    obj=Prediction()
    obj.predict()
