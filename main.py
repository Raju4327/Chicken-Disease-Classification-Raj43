from cnnClassifier import logger
from cnnClassifier.pipeline.stage_o1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline  



STAGE_NAME='Data Ingestion stage'

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME='Prepare Base Model'

if __name__=='__main__':
    try:
        logger.info(f"*****************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME='Training'

if __name__=='__main__':
    try:
        logger.info(f"*****************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
