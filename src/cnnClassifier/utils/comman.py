import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path) ->ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml(str):path like input
    Raises:
        ValueError:if yaml file is empty
        a:empty file
    Retruns:
        CongigBox:ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise valueError('yaml file is empty')
    except exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verboss=True):
    """ Create list of directories

    Args:
         path_to_directories(list): list of path of directories
         ignore_log(bool,optional): ignore if multiple dires is to be created.Defaults to False
    """
    for path in path_to_directories:
        os_make_dirs(path,exist_ok=True)
        if verboss:
            logger.info(f"Created directories at :{path}")
@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data

    Args:
        path(Path):path to json file
        data(dict):data to b saved in json file
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at : {path}")


@ensure_annotations
def load_json(path:Path)->CofigBox:
    """load json file data
    Args:
        path(Path):path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file loadded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """ save binary file

    Args:
       data (Any):data to be saved as binary
       path(Path):path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at : {path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data

    Args:
        path(Path):path to binary file
    Returns:
         Any: object sotred in the file
    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from :{path}")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    """ get size in KB
    Args:
        path(Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb=round(os.path.getsize(pat)/1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read)
        