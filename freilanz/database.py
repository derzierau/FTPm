import pandas as pd
import tempfile
import sqlite3
import os
from freilanz.helper import DIRS, ACTION_TYPES
from freilanz.config import Config, get_config

columns = columns = ['id', 'profile', 'project',
                     'path', 'timestamp', 'message', 'service', 'action']


class Database:
    def __init__(self):
        self.config = get_config()
        try:
            os.makedirs(f"{DIRS.user_data_dir}")
        except:
            pass
        # self.cursor = None
        self.conn = sqlite3.connect(f"{DIRS.user_data_dir}/db.db")
        if self.conn:
            self.cursor = self.conn.cursor()
            self.initialize()

    def initialize(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS times
             (id INTEGER PRIMARY KEY AUTOINCREMENT, profile text, project text, path text, timestamp text, message text, service text, action text)''')

        return self.commit()

    def commit(self):
        return self.conn.commit()

    def get_snapshot(self):
        try:
            data = self.cursor.execute('SELECT * FROM times').fetchall()

            if len(data) == 0:
                return pd.DataFrame()

            data = pd.DataFrame(data, columns=columns)
            data['timestamp'] = pd.to_datetime(
                data['timestamp'],  infer_datetime_format=True)
            data.set_index(['id'])
            return data

        except FileNotFoundError as error:
            pass

    def update(self, id: int):
        pass

    def insert(self, entry):
        sql = "INSERT INTO times (profile, project, path, timestamp, message, service, action) VALUES (?,?,?,?,?,?,?)"

        self.cursor.execute(sql, (entry['profile'], entry['project'], entry['path'],
                                  entry['timestamp'], entry['message'], entry['service'], entry['action']))
        self.commit()

        return self

    def get(self):
        return self.get_snapshot()

    def save(self, frame: pd.DataFrame):

        sql = frame.to_sql('times', con=self.conn, if_exists='replace')

        self.commit()
        print(self.get())
        # frame.to_hdf(DB_PATH_HD5, 'table', append=True, index=False, data_columns=True)

    def get_sum_by_profile_project(self, profile, project):
        data = self.get()
        config = Config()
        data = data[data['profile'] == profile]
        data['duration'] = data['timestamp'].diff()
        query = data.action.str.contains(
            ACTION_TYPES['end']) & data.profile.str.contains(profile)

        if project:
            query = query & data.project.str.contains(
                project)

        data = data[query]
        _group_by = data.groupby(
            ['service', pd.Grouper(freq='M', key='timestamp')])['duration'].sum()
        positions = {}
        for index in _group_by.groupby()
        return _group_by.to_string()

    def open_timer(self):
        query = self.cursor.execute(
            'SELECT * FROM times WHERE timestamp IS NULL')
        snapshot = self.get_snapshot()
        if not snapshot.empty:
            _group_by_profile = snapshot.groupby(
                ['profile']).last()
            return _group_by_profile[_group_by_profile['action'] == 'start']

        return pd.DataFrame()
