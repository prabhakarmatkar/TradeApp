from nse.nse import NseInitializer
nse = NseInitializer()


def socket_event_listener(sio,nse_poller):
    active_sessions = []
    watch_list_to_poll = {}

    def add_active_session(sid):
        active_sessions.append(sid)
        nse_poller.update_active_sessions(updated_active_sessions=active_sessions)

    def delete_active_session(sid):
        active_sessions.__delitem__(sid)
        nse_poller.update_active_sessions(updated_active_sessions=active_sessions)

    @sio.event
    def connect(sid, data):
        print("user connected", sid)
        add_active_session(sid=sid)

    @sio.event
    def disconnect(sid):
        print("user disconnected", sid)
        sio.close_room(sid)
        delete_active_session(sid)

    @sio.on('fetch-all-stocks')
    def fetch_all_stocks(sid, data):
        print('event received', sid)
        all_stock_codes = nse.get_stock_codes()
        sio.emit(event='refresh-data', data=all_stock_codes, to=sid)

    @sio.on('fetch-watchlist-stocks')
    def fetch_all_stocks(sid, watchlist):
        print('event received', watchlist)
        update_watch_list_to_poll(sid, watchlist)

    def update_watch_list_to_poll(sid, watchlist):
        for x in watchlist:
            if x in watch_list_to_poll.keys():
                subscribers = watch_list_to_poll.get(x)
                if sid not in subscribers:
                    subscribers.append(sid)
            else:
                watch_list_to_poll.__setitem__(x, [sid])
        nse_poller.update_watch_list_to_poll(updated_watch_list_to_poll=watch_list_to_poll)
