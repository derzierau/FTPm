import os 
from helper import split

class Project():
  def __init__(self):
    self.current_path = os.getcwd()
    self.current_project = split(self.current_path)[-1]
    self.current_account = split(split(self.current_path)[-2])[-1]