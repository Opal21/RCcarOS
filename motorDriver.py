import RPi.GPIO as GPIO

REAR_RIGHT_MOTOR_ENABLE_PIN = 22
REAR_RIGHT_MOTOR_DATA_ONE = 27
REAR_RIGHT_MOTOR_DATA_TWO = 17

FRONT_RIGHT_MOTOR_ENABLE_PIN = 21
FRONT_RIGHT_MOTOR_DATA_ONE = 20
FRONT_RIGHT_MOTOR_DATA_TWO = 16

REAR_LEFT_MOTOR_ENABLE_PIN = 13
REAR_LEFT_MOTOR_DATA_ONE = 26
REAR_LEFT_MOTOR_DATA_TWO = 19

FRONT_LEFT_MOTOR_ENABLE_PIN = 0
FRONT_LEFT_MOTOR_DATA_ONE = 5
FRONT_LEFT_MOTOR_DATA_TWO = 6

PWM_FREQUENCY = 1000
INITIAL_PWM_DUTY_CYCLE = 100


def set_gpio_pins():
    """Sets the GPIO pins for the two motors"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FRONT_RIGHT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(FRONT_RIGHT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(FRONT_LEFT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(FRONT_LEFT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(REAR_RIGHT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(REAR_RIGHT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(REAR_LEFT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(REAR_LEFT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(FRONT_RIGHT_MOTOR_ENABLE_PIN, GPIO.OUT)
    GPIO.setup(FRONT_LEFT_MOTOR_ENABLE_PIN, GPIO.OUT)
    GPIO.setup(REAR_RIGHT_MOTOR_ENABLE_PIN, GPIO.OUT)
    GPIO.setup(REAR_LEFT_MOTOR_ENABLE_PIN, GPIO.OUT)


def set_idle_mode():
    """Set mode to Idle"""
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_TWO, True)
    GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, True)


def go_forward():
    """Set mode to Forward"""
    set_fr(True)
    set_rr(True)
    set_fl(True)
    set_rl(True)


def go_reverse():
    """Set mode to Reverse"""
    set_fr(False)
    set_rr(False)
    set_fl(False)
    set_rl(False)


def turn_right():
    """Set mode to Right"""
    set_fr(False)
    set_rr(False)
    set_fl(True)
    set_rl(True)


def turn_left():
    """Set mode to Left"""
    set_fr(True)
    set_rr(True)
    set_fl(False)
    set_rl(False)


def go_right():
    set_fr(False)
    set_rr(True)
    set_fl(True)
    set_rl(False)


def go_left():
    set_fr(True)
    set_rr(False)
    set_fl(False)
    set_rl(True)


def go_front_left():
    set_rr(True)
    set_fl(True)


def go_front_right():
    set_rl(True)
    set_fr(True)


def set_fr(forward: bool):
    if forward:
        GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, True)
        GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, False)
    else:
        GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, False)
        GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, True)


def set_rr(forward: bool):
    if forward:
        GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, False)
        GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, True)
    else:
        GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, True)
        GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, False)


def set_fl(forward: bool):
    if forward:
        GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, True)
        GPIO.output(FRONT_LEFT_MOTOR_DATA_TWO, False)
    else:
        GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, False)
        GPIO.output(FRONT_LEFT_MOTOR_DATA_TWO, True)


def set_rl(forward: bool):
    if forward:
        GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, False)
        GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, True)
    else:
        GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, True)
        GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, False)
