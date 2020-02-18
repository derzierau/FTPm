from lancelot.config import get_config

class Services():
  def __init__(self):
    self.services = get_config()['services']
    print(services)