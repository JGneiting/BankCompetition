import server
from flask import request


@server.app.route('/bankcompetition/home')
def home():
    print("HELLO")
    return "Hello, world!"

@server.socketio.on('connect')
def handle_connect():
    print('connected')
    # server.socketio.emit('agent_info', {'data': "Please send your agent name"}, room=request.sid)

@server.socketio.on('agent_info')
def handle_agent_info(data):
    print('received agent info: ' + data)
    server.room.add_player(request.sid, data)

@server.socketio.on('poll-response')
def handle_poll_response(data):
    print('received poll response: ' + data)
    server.room.message_received(request.sid, data)

@server.socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    server.socketio.emit("Echo: " + message)
