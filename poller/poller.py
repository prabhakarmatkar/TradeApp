import time
from nse.nse import NseInitializer


class NsePoller:
    def __init__(self,sio):
        self.watch_list_to_poll = {}
        self.active_sessions = []
        self.sio = sio
        self.nse = NseInitializer()

    def update_watch_list_to_poll(self,updated_watch_list_to_poll):
        self.watch_list_to_poll = updated_watch_list_to_poll

    def update_active_sessions(self,updated_active_sessions):
        self.active_sessions = updated_active_sessions

    def nse_get_stock_quote(self):
        while True:
            self.nse_poller(watch_list=self.watch_list_to_poll,active_sessions=self.active_sessions)
            time.sleep(1)

    def nse_poller(self,watch_list,active_sessions):
        print('pooling', watch_list)
        for x in watch_list.keys():
            watch_list_stocks = self.nse.get_quote(x)
            for subscriber in watch_list[x]:
                if subscriber in active_sessions:
                    self.sio.emit(event='refresh-data', data=watch_list_stocks, to=subscriber)
