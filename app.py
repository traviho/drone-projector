# unused

from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return 'Welcome'

@app.route('/api/direction', methods=['POST'])
def api_direction():
	req_data = request.form
	print(req_data['number'])
	emit('direction', req_data['number'])
	return 'something'

if __name__ == '__main__':
    socketio.run(app)
