from database import Database
import pandas as pd
class Stats:
  def __init__(self):
    self.db = Database()

  def filtered(self):
    return self.db.get()
  
  def duration_sum_by_key(self, key = 'project'):
    data = self.filtered()
    _data = pd.DataFrame()
    data['duration'] = data.sort_values(['timestamp']).groupby(key)['timestamp'].diff()
    for i, frame in data.groupby([key]):
      _data = _data.append({
        key: i,
        'sum': frame['duration'].sum()
      }, ignore_index=True)

    return _data