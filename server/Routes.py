import server


@server.app.route('/bankcompetition')
def home():
    return "Hello, world!"


@server.socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    server.socketio.send("Echo: " + message)
