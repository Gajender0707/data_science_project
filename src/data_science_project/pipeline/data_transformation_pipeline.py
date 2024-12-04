from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transfomation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.data_splitting()



# if __name__=="__main__":
#     obj=DataTransformationPipeline()
#     obj.initiate_data_transformation()