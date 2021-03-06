from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

# escuchar evento message que viene del cliente

@socketio.on('message')
def handleMessage(msg):
	print('message ' + msg)
	send(msg, broadcast = True)


if __name__ == '__main__':
	socketio.run(app, debug = True)