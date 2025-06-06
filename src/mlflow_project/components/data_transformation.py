import os
from mlflow_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlflow_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    # Note: Different data transformation techniques can be used - such as Scaler, PCA 
    # All kinds of EDA can be performed in ML cycle - before passing data to the model

    def split_data_train_test(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)