from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.model_evaluation import ModelEvaluation
from mlflow_project import logger

STAGE_NAME = "Stage 5 - Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} - started")
        eval = ModelEvaluationPipeline()
        eval.main()
        logger.info(f"Stage: {STAGE_NAME} - completed")
    
    except Exception as e:
        logger.exception(e)
        raise e
