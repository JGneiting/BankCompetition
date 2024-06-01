import server


@server.app.route('/bankcompetition/home')
def home():
    print("HELLO")
    return "Hello, world!"


@server.socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    server.socketio.emit("Echo: " + message)
