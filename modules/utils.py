# Python Library Imports
import logging
import os
import json
from subprocess import Popen
from typing import Type, Union, Dict, Any


def load_json(path_to_json: str) -> Dict[str, Any]:
    """
    Purpose:
        Load json files
    Args:
        path_to_json (String): Path to  json file
    Returns:
        Conf: JSON file if loaded, else None
    """
    try:
        with open(path_to_json, "r") as config_file:
            conf = json.load(config_file)
            return conf

    except Exception as error:
        logging.error(error)
        raise TypeError("Invalid JSON file")


def save_json(json_path: str, json_data: Any) -> None:
    """
    Purpose:
        Save json files
    Args:
        path_to_json (String): Path to  json file
        json_data: Data to save
    Returns:
        N/A
    """
    try:
        with open(json_path, "w") as outfile:
            json.dump(json_data, outfile)
    except Exception as error:
        raise OSError(error)


def append_to_file(file_path: str, file_text: str) -> bool:
    """
    Purpose:
        Append text to a file
    Args/Requests:
         file_path: file path
         file_text: Text of file
    Return:
        Status: True if appended, False if failed
    """

    try:
        with open(file_path, "a") as myfile:
            myfile.write(file_text)
            return True

    except Exception as error:
        logging.error(error)
        return False


def read_from_file(file_path: str) -> str:
    """
    Purpose:
        Read data from a file
    Args/Requests:
         file_path: file path
    Return:
        read_data: Text from file
    """
    try:
        with open(file_path) as f:
            read_data = f.read()

    except Exception as error:
        logging.error(error)
        return None

    return read_data


def write_to_file(file_path: str, file_text: str) -> bool:
    """
    Purpose:
        Write text from a file
    Args/Requests:
         file_path: file path
         file_text: Text of file
    Return:
        Status: True if appened, False if failed
    """

    try:
        with open(file_path, "w") as myfile:
            myfile.write(file_text)
            return True

    except Exception as error:
        logging.error(error)
        return False
