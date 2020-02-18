import pandas as pd
import tempfile
from FTPm.helper import DB_PATH, START_TIMER_ACTION, END_TIMER_ACTION, DB_PATH_HD5
from FTPm.config import get_config


class Database:
    def __init__(self):
        self.config = get_config()
        # self.store = pd.HDFStore('store.h5')

    def get_snapshot(self):
        try:
            data = pd.read_csv(DB_PATH, parse_dates=['timestamp'])
            return data

        except FileNotFoundError as error:
            return pd.DataFrame()

    def insert(self, entry):
        snapshot = self.get_snapshot()
        _snapshot = snapshot.append(entry)
        self.save(_snapshot)

        return _snapshot
    def get(self):
      return self.get_snapshot()

    
    def save(self, frame: pd.DataFrame):
        frame.to_csv(DB_PATH, index=False)
        # frame.to_hdf(DB_PATH_HD5, 'table', append=True, index=False, data_columns=True)


    def open_timer(self):

        snapshot = self.get_snapshot()
        if not snapshot.empty:
          _groupedByProject = snapshot.groupby(
              ['path', 'account', 'project']).last()
          return _groupedByProject[_groupedByProject['action'] == START_TIMER_ACTION]

        return pd.DataFrame()