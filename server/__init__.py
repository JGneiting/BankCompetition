from flask import Flask
from flask_socketio import SocketIO
from server.ServerGame import ServerRoom


app = Flask("BANK Server")
socketio = SocketIO(app)
room = ServerRoom()

import server.Routes as routes

if __name__ == "__main__":
    socketio.run(app)
