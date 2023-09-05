import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.comman import save_json

from urllib.parse import urlparse

class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config
    
    def _valid_generator(self):

        datagenerator_kwargs=dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs=dict(
            target_size=self.config.params_image_sizeL[:-1],
            interpoation='bilinear'
        )

        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator=valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )
    @staticmethod
    def load_model(path,Path)->tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model=self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score=model.evaluate(self.valild_generator)

    def save_score(self):
        scores={"loss":self.score[0],"accuracy":self.score[1]}
        save_json(path=Path('score.json'),data=scores)
