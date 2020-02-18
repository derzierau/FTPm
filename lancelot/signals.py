import signal


class Signals:
    def __init__(self):
        while True:
            signal.signal(signal.SIGTERM, self.on_shutdown)
            signal.signal(signal.SIGQUIT, self.on_shutdown)

    def on_shutdown(self):
        print('DOWN')
