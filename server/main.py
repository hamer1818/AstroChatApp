# server.py
from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store connected users
users = []

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

def handle_join(username, avatar=None):
    users.append({'id': request.sid, 'username': username, 'avatar': avatar})
    socketio.emit('userList', users)

@socketio.on('join')
def on_join(data):
    username = data.get('username')
    avatar = data.get('avatar')
    handle_join(username, avatar)

@socketio.on('message')
def handle_message(data):
    # print(f'Message from {request.sid}: {data}')
    socketio.emit('message', {
        'userId': request.sid,
        'username': data['username'],
        'message': data['message'],
        'timestamp': datetime.now().isoformat(),
        'avatar': data['avatar']
    })

@socketio.on('disconnect')
def handle_disconnect():
    global users
    users = [user for user in users if user['id'] != request.sid]
    socketio.emit('userList', users)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)