from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlflow_project.pipeline.stage_02_data_validation import DataValidationPipeline
from mlflow_project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlflow_project.pipeline.stage_04_model_trainer import ModelTrainerPipeline
# logger.info("Welcome to our project!")


# 01 STAGE - INGESTION
STAGE_NAME = "Stage 1 - Data Ingestion"
try:
    logger.info(f"Stage: {STAGE_NAME} - started")
    ingest = DataIngestionPipeline()
    ingest.main()
    logger.info(f"Stage: {STAGE_NAME} - completed")

except Exception as e:
    logger.exception(e)
    raise e


# 02 STAGE - VALIDATION
STAGE_NAME = "Stage 2 - Data Validation"
try:
    logger.info(f"Stage: {STAGE_NAME} - started")
    valid = DataValidationPipeline()
    valid.main()
    logger.info(f"Stage: {STAGE_NAME} - completed")

except Exception as e:
    logger.exception(e)
    raise e


# 03 STAGE - TRANSFORMATION
STAGE_NAME = "Stage 3 - Data Transformation"
try:
    logger.info(f"Stage: {STAGE_NAME} - started")
    transform = DataTransformationPipeline()
    transform.main()
    logger.info(f"Stage: {STAGE_NAME} - completed")

except Exception as e:
    logger.exception(e)
    raise e


# 04 STAGE - TRAINING
STAGE_NAME = "Stage 4 - Model Training"
try:
    logger.info(f"Stage: {STAGE_NAME} - started")
    valid = ModelTrainerPipeline()
    valid.main()
    logger.info(f"Stage: {STAGE_NAME} - completed")

except Exception as e:
    logger.exception(e)
    raise e
