from lancelot.config import get_config



class Integrations:
  def __init__(self):
    self.config = get_config()['integrations']
  
class SevDeskIntegration(Integrations):
  def __init__(self):
    super()
    self.authQuery = {
      'token': self.config['sevDesk']['API_TOKEN']
    }