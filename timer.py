from project_manager import Project
from datetime import datetime
import pandas as pd
from helper import DB_PATH

START_TIMER_ACTION = 'start_timer_action'
END_TIMER_ACTION = 'end_timer_action'


def start_time(project=None):
    project = Project().current_project
    account = Project().current_account
    timestamp = datetime.now()
    entry = pd.DataFrame({
      'project': [project],
      'account': [account],
      'timestamp': [timestamp],
      'action': [START_TIMER_ACTION],
    })
    try:
        db = pd.read_csv(DB_PATH)
        print(db)

        _db = db.append(entry)
        _db.to_csv(DB_PATH, index=False)
        print(_db)

    except:
        print(entry)

        entry.to_csv(DB_PATH, index=False)
    
    return {
        'project': project,
        'account': account,
        'timestamp': timestamp
    }
