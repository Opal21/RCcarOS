import RPi.GPIO as GPIO

FRONT_RIGHT_MOTOR_ENABLE_PIN = 22
FRONT_RIGHT_MOTOR_DATA_ONE = 27
FRONT_RIGHT_MOTOR_DATA_TWO = 17
REAR_RIGHT_MOTOR_ENABLE_PIN = 2  # TBW
REAR_RIGHT_MOTOR_DATA_ONE = 3  # TBW
REAR_RIGHT_MOTOR_DATA_TWO = 4  # TBW
REAR_LEFT_MOTOR_ENABLE_PIN = 13
REAR_LEFT_MOTOR_DATA_ONE = 26
REAR_LEFT_MOTOR_DATA_TWO = 19
FRONT_LEFT_MOTOR_ENABLE_PIN = 0  # TBW
FRONT_LEFT_MOTOR_DATA_ONE = 5  # TBW
FRONT_LEFT_MOTOR_DATA_TWO = 6  # TBW
PWM_FREQUENCY = 1000
INITIAL_PWM_DUTY_CYCLE = 100


def set_right_mode():
    """Set mode to Right"""
    # GPIO.output(LEFT_FRONT_MOTOR_DATA_ONE, True)
    # GPIO.output(LEFT_FRONT_MOTOR_DATA_TWO, False)
    # GPIO.output(RIGHT_MOTOR_DATA_ONE, False)
    # GPIO.output(RIGHT_MOTOR_DATA_TWO, True)


def set_left_mode():
    """Set mode to Left"""
    # GPIO.output(LEFT_FRONT_MOTOR_DATA_ONE, False)
    # GPIO.output(LEFT_FRONT_MOTOR_DATA_TWO, True)
    # GPIO.output(RIGHT_MOTOR_DATA_ONE, True)
    # GPIO.output(RIGHT_MOTOR_DATA_TWO, False)


def set_reverse_mode():
    """Set mode to Reverse"""
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, False)
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, False)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_TWO, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, False)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, True)
    GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, False)
    GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, True)


def set_forward_mode():
    """Set mode to Forward"""
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, False)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, False)
    GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, False)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, False)


def set_idle_mode():
    """Set mode to Idle"""
    set_right_motor_to_idle()
    set_left_motor_to_idle()


def set_right_motor_to_idle():
    """Sets the RIGHT motor to Idle state"""
    GPIO.output(REAR_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_LEFT_MOTOR_DATA_TWO, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(REAR_RIGHT_MOTOR_DATA_TWO, True)


def set_left_motor_to_idle():
    """Sets the LEFT motor to Idle state"""
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_RIGHT_MOTOR_DATA_TWO, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(FRONT_LEFT_MOTOR_DATA_ONE, True)


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
