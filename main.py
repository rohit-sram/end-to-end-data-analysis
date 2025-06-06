from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline

# logger.info("Welcome to our project!")

STAGE_NAME = "Stage 1 - Data Ingestion"

try:
    logger.info(f"Stage: {STAGE_NAME} - started")
    ingest = DataIngestionPipeline()
    ingest.main()
    logger.info(f"Stage: {STAGE_NAME} - completed")

except Exception as e:
    logger.exception(e)
    raise e