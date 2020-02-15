from database import Database
class Stats:
  def __init__(self):
    self.db = Database()

  def filtered(self):
    return self.db.get()