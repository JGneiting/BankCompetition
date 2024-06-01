from flask import Flask
from flask_socketio import SocketIO


app = Flask("BANK Server")
socketio = SocketIO(app)

import server.Routes as routes

if __name__ == "__main__":
    app.run(debug=True)
