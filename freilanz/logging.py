import logging
import os
from freilanz.helper import log_dir

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.FileHandler(filename=f'{log_dir}/logs.log')



def logger(name):
  return logging.getLogger(name)