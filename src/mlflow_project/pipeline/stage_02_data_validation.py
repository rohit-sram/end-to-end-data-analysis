from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_validation import DataValidation
from mlflow_project import logger

STAGE_NAME = "Stage 2 - Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validatiion_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_validatiion_config)
        data_ingestion.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} - started")
        valid = DataValidationPipeline()
        valid.main()
        logger.info(f"Stage: {STAGE_NAME} - completed")
    
    except Exception as e:
        logger.exception(e)
        raise e