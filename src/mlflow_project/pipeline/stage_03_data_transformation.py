from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_transformation import DataTransformation
from mlflow_project import logger
from pathlib import Path

STAGE_NAME = "Stage 3 - Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_data_train_test()
            else:
                raise Exception("The data schema was not valid.")
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} - started")
        transform = DataTransformationPipeline()
        transform.main()
        logger.info(f"Stage: {STAGE_NAME} - completed")
    
    except Exception as e:
        logger.exception(e)
        raise e