from config import get_config
import pandas as pd
import tempfile
from helper import DB_PATH

class Database:
  def __init__(self):
    self.config = get_config()

  def get_snapshot(self):
    return pd.read_csv(DB_PATH)
    
  def save(self, frame: pd.DataFrame):
     frame.to_csv(DB_PATH, index=False)
  
