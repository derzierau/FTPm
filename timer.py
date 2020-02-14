from project_manager import Project
from datetime import datetime
import pandas as pd
from helper import DB_PATH
from database import Database

START_TIMER_ACTION = 'start_timer_action'
END_TIMER_ACTION = 'end_timer_action'


class Timer:
    def __init__(self):
        self.project = Project().current_project
        self.account = Project().current_account
        self.db = Database()

    def end_timer(self):
        raise NotImplementedError

    def start_time(self, project=None):
        timestamp = datetime.now()
        entry = pd.DataFrame({
            'project': [project],
            'account': [account],
            'timestamp': [timestamp],
            'action': [START_TIMER_ACTION],
        })
        try:
            snapshot = self.db.get_snapshot()
            _snapshot = snapshot.append(entry)
            self.db.save(_snapshot)
        except:
            self.db.save(entry)

        return {
            'project': project,
            'account': account,
            'timestamp': timestamp
        }
