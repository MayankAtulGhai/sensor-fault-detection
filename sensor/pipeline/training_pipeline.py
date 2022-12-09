from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging

class TrainPipeline:

    def __init__(self):
        trainig_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainig_pipeline_config)
        self.trainig_pipeline_config = trainig_pipeline_config


    def start_date_ingestion(self): #DataIngestionArtifact will be returned
        try:
            logging.info("Starting Data Ingestion") 
            logging.info("Data Ingestion Completed") 
        except Exception as e:
            raise SensorException(e, sys)

    def start_date_validation(self):
        try:
            pass 
        except Exception as e:
            raise SensorException(e, sys)

    def start_date_transformation(self):
        try:
            pass 
        except Exception as e:
            raise SensorException(e, sys)
    
    def start_model_trainer(self):
        try:
            pass 
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_pusher(self):
        try:
            pass 
        except Exception as e:
            raise SensorException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_date_ingestion() 
        except Exception as e:
            raise SensorException(e, sys)