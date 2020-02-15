from project_manager import Project
from datetime import datetime
import pandas as pd
from helper import DB_PATH, START_TIMER_ACTION, END_TIMER_ACTION
from database import Database
from config import Config
import logging

log = logging.getLogger(__name__)


class Timer:
    def __init__(self):
        self.project = Project().current_project
        self.account = Project().current_account
        self.current_path = Project().current_path
        self.config = Config()
        self.db = Database()

    def entry(self, action, *args, **kwargs):
        timestamp = datetime.now()
        return pd.DataFrame({
            'project': [kwargs.get('project', self.project)],
            'account': [kwargs.get('account', self.account)],
            'path': [kwargs.get('path', self.current_path)],
            'service': [kwargs.get('service', self.config.default_service()['short_name'])],
            'message': [kwargs.get('message', None)],
            'timestamp': [timestamp],
            'action': [action],
        })

    def end_timer(self):
        # First end all open timer
        timers = self.db.open_timer()
        if not timers.empty:
            if len(timers.index) > 1:
                for index, timer in timers.reset_index().iterrows():
                    entry = self.entry(
                        END_TIMER_ACTION, project=timer['project'], account=timer['account'], path=timer['path'])
                    self.db.insert(entry)
            else:
                val = timers.reset_index().iloc[0]
                self.db.insert(self.entry(
                    END_TIMER_ACTION, project=val['project'], account=val['account'], path=val['path']))
            return timers.reset_index().to_dict('records')
        else:
            log.debug(f'No timer was started for {self.current_path}')


    def start_time(self, message, service, account, project):
        # Close all timer
        self.end_timer()
        
        params = {}
        
        if message:
            params['message'] = message
        if service:
            params['service'] = service
        if account:
            params['account'] = account
        if project:
            params['project'] = project


        entry = self.entry(START_TIMER_ACTION, **params)
        try:
            self.db.insert(entry)
        except:
            self.db.save(entry)

        return {
            'project': self.project,
            'account': self.account,
            'path': self.current_path,
            'timestamp': entry['timestamp']
        }
