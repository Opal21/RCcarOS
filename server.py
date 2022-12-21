from enum import Enum

import RPi.GPIO as GPIO
import cv2
from flask import Flask, render_template, Response
from flask_socketio import SocketIO

import motorDriver


class Directions(Enum):
    STOP = 0
    FORWARD = 1
    BACKWARD = 2
    RIGHT = 3
    LEFT = 4
    FRONT_RIGHT = 5
    FRONT_LEFT = 6
    TURN_RIGHT = 7
    TURN_LEFT = 8
    REAR_RIGHT = 9
    REAR_LEFT = 10


app = Flask(__name__)
socket_ = SocketIO(app, async_mode=None)

motorDriver.set_gpio_pins()

pwm_front_left = GPIO.PWM(motorDriver.FRONT_LEFT_MOTOR_ENABLE_PIN, motorDriver.PWM_FREQUENCY)
pwm_front_left.start(motorDriver.INITIAL_PWM_DUTY_CYCLE)

pwm_rear_left = GPIO.PWM(motorDriver.REAR_LEFT_MOTOR_ENABLE_PIN, motorDriver.PWM_FREQUENCY)
pwm_rear_left.start(motorDriver.INITIAL_PWM_DUTY_CYCLE)

pwm_front_right = GPIO.PWM(motorDriver.FRONT_RIGHT_MOTOR_ENABLE_PIN, motorDriver.PWM_FREQUENCY)
pwm_front_right.start(motorDriver.INITIAL_PWM_DUTY_CYCLE)

pwm_rear_right = GPIO.PWM(motorDriver.REAR_RIGHT_MOTOR_ENABLE_PIN, motorDriver.PWM_FREQUENCY)
pwm_rear_right.start(motorDriver.INITIAL_PWM_DUTY_CYCLE)

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


# listeners to the client requests
@socket_.on('ConnectionCheck')
def test_message(message):
    print(message)


@socket_.on('forwards')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.FORWARD)


@socket_.on('backwards')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.BACKWARD)


@socket_.on('left')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.LEFT)


@socket_.on('right')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.RIGHT)


@socket_.on('up-left')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.FRONT_LEFT)


@socket_.on('up-right')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.FRONT_RIGHT)


@socket_.on('down-left')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.REAR_LEFT)


@socket_.on('down-right')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.REAR_RIGHT)


@socket_.on('stop')
def handle_message(data):
    print('received message: ' + data)
    set_direction(Directions.STOP)


def set_direction(direction):
    if direction == Directions.FORWARD:
        motorDriver.go_forward()
    elif direction == Directions.BACKWARD:
        motorDriver.go_reverse()
    elif direction == Directions.LEFT:
        motorDriver.turn_left()
    elif direction == Directions.RIGHT:
        motorDriver.turn_right()
    elif direction == Directions.FRONT_LEFT:
        motorDriver.go_front_left()
    elif direction == Directions.FRONT_RIGHT:
        motorDriver.go_front_right()
    elif direction == Directions.REAR_LEFT:
        motorDriver.go_rear_left()
    elif direction == Directions.REAR_RIGHT:
        motorDriver.go_rear_right()
    else:
        motorDriver.set_idle_mode()


if __name__ == '__main__':
    socket_.run(app, host='0.0.0.0', allow_unsafe_werkzeug=True)
