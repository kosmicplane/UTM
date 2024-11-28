import logging
from src.api import ALTITUDAPI

# Creating a base logger with default formatting that logs to the log.log inside output folder.
base_logger = logging.getLogger('base')
base_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler = logging.FileHandler('../output/log.log')
streamHandler = logging.StreamHandler()
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
base_logger.addHandler(fileHandler)
base_logger.addHandler(streamHandler)

"""
Class intended to add a new children of the base logger when the constructor is called.
"""
class AuxiliaryLogger:
  
    def __init__(self, name: str = "default") -> None:
        self.name = name
        self.logger = logging.getLogger(f"base.auxiliary.{self.name.capitalize()}")
        self.logger.setLevel(0)
        







