from flask import Flask, render_template,Response, session
from flask_socketio import SocketIO
import cv2



async_mode = None
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)


camera=cv2.VideoCapture(0)
def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

## listeners to the client requests
@socket_.on('my_event')
def test_message(message):
    print(message)

@socket_.on('custom-event1')
def handle_message(data):
    print('received message: ' + data)

@socket_.on('custom-event2')
def handle_message(data):
    print('received message: ' + data)

@socket_.on('custom-event3')
def handle_message(data):
    print('received message: ' + data)

@socket_.on('custom-event4')
def handle_message(data):
    print('received message: ' + data)

@socket_.on('custom-event5')
def handle_message(data):
    print('received message: ' + data)

if __name__ == '__main__':
    socket_.run(app, host='0.0.0.0', debug=True)
