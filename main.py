import logging
import threading
import server
from socket_listener.socket_listener import socket_event_listener
from poller.poller import NsePoller

sio = server.get_socket()
app = server.get_app(sio)
nse_poller = NsePoller(sio)
socket_event_listener(sio, nse_poller)

try:
    x = threading.Thread(target=nse_poller.nse_get_stock_quote, args=())
    logging.info("Main    : before running thread")
    x.start()
except:
    print('Error occured..')

if __name__ == '__main__':
    # get_stock_quote(watch_list_to_poll=watch_list_to_poll)
    # app.run(port=8000)
    print('Server started....')
    print('Listening to http://localhost:8000')
