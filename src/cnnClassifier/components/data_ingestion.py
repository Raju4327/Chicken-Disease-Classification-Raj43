import os 
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.comman import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __int__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info:\n{headers}")
        else:
            logger.info(f"file already exists of size : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path:str
        extracts the zip file into the data directory
        function returns None
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exists_ok=True)
        with zipfile.zipfile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)



