from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging
from sensor.components .data_ingestion import DataIngestion

class TrainPipeline:

    def __init__(self):
        self.trainig_pipeline_config = TrainingPipelineConfig()
       


    def start_date_ingestion(self): #DataIngestionArtifact will be returned
        try:

            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.trainig_pipeline_config)
            logging.info("Starting Data Ingestion") 
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion() 
            logging.info(f"Data Ingestion Completed and artifact: {data_ingestion_artifact}") 
            return data_ingestion_artifact

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