from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

# Init the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def root():
    """ Send HTML from the server."""
    return render_template('chat.html')

@socketio.on('message')   
def message_recieved(message):
    """
    Called when the user sends a message.
    """ 
    print(message)

    # Send message back
    emit('send_message_function', {"data":"some message"})

if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=5000)