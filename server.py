import socketio


def get_app(sio):
    # create a Socket.IO server
    app = socketio.WSGIApp(sio)
    return app


def get_socket():
    sio = socketio.Server(cors_allowed_origins='*')
    return sio
