import signal
import os
from freilanz.timer import Timer

class Signals:
    def __init__(self):
        print(os.getpid())
        while True:
            signal.signal(signal.SIGTERM, self.on_shutdown)
            signal.signal(signal.SIGQUIT, self.on_shutdown)

    def on_shutdown(self, *args, **kwargs):
        Timer().end_timer()
