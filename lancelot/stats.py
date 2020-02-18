from lancelot.database import Database
import pandas as pd
import logging
from lancelot.config import Config
from lancelot.project_manager import Project
log = logging.getLogger(__name__)


class Stats:
    def __init__(self):
        self.db = Database()
        

    def filtered(self):
        return self.db.get()

    def duration_sum_by_key(self, key='project'):
        data = self.filtered()
        _data = pd.DataFrame()
        config = Config()

        data['duration'] = data.sort_values(['timestamp']).groupby(key)[
            'timestamp'].diff()
        for i, frame in data.groupby([key, 'service', 'account']):
            duration_sum = frame['duration'].sum()
            total_seconds = duration_sum.total_seconds()
            hour_rate = 50
            
            service_rate = config.get_services(short_name=i[1])

            if 'base_hourly_rate' in service_rate:
              hour_rate = service_rate['base_hourly_rate']
            
            _data = _data.append({
                key: i[0],
                'service': i[1],
                'account': i[2],
                'sum': duration_sum,
                'hours': total_seconds//3600,
                'rate': hour_rate
            }, ignore_index=True)
            
        
        _data['revenue'] = (_data['sum'].astype('timedelta64[m]') * _data['rate']) / 60
        
        return _data.set_index([key,'service', 'account'])
