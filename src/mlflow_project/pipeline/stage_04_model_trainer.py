from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.model_trainer import ModelTrainer
from mlflow_project import logger
from pathlib import Path

STAGE_NAME = "Stage 4 - Model Training"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
    

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} - started")
        trainer = ModelTrainerPipeline()
        trainer.main()
        logger.info(f"Stage: {STAGE_NAME} - completed")
    
    except Exception as e:
        logger.exception(e)
        raise e