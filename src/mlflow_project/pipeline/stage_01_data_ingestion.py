from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_ingestion import DataIngestion
from mlflow_project import logger

STAGE_NAME = "Stage 1 - Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} - started")
        ingest = DataIngestionPipeline()
        ingest.main()
        logger.info(f"Stage: {STAGE_NAME} - completed")
    
    except Exception as e:
        logger.exception(e)
        raise e