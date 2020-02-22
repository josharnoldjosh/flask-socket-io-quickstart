from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
# from gevent import monkey
# monkey.patch_all()

# Init the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True)

@app.route('/')
def root():
    """ Send HTML from the server."""
    return render_template('index.html')

@app.route('/<email>/<game_id>/<user_type>')
def game(email, game_id, user_type):
    if user_type == "drawer":
        return render_template('drawer.html', game_id=game_id)
    else:
        return render_template('teller.html', game_id=game_id)

@socketio.on('message')   
def message_recieved(message):    
    emit('display_message', message, broadcast=True)
    

if __name__ == '__main__':
    """ Run the app. """    
    socketio.run(app, port=2000, debug=True, threaded=True)
    # socketio.run(app, port=2000)