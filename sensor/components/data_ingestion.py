from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from pandas import Dataframe


class DataIngestion:

     def __init__(self, data_ingestion_config:DataIngestionConfig):

        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_faeture_store(self) -> DataFrame:

    '''
    Export mongodb collection record as data frame into feature
    '''
        pass

    def split_data as train_test(self, dataframe: Dataframe) -> None:
        '''Feature stored dataset will be split into train and test file

        '''
        pass

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
         
        try:
            pass 
        except Exception as e:
            raise SensorException(e, sys)

