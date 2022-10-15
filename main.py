import motorDriver

import threading
import requests
import time
import cv2 as cv

from enum import Enum


class Directions(Enum):
    STOP = 0
    FORWARD = 1
    BACKWARD = 2
    RIGHT = 3
    LEFT = 4


class RCcarOS:
    def __init__(self):
        self.currentDirection = Directions.STOP

    def get_direction(self):
        direction = requests.get('https://w3schools.com/python/demopage.htm')
        self.currentDirection = direction

    def move_car(self):
        match self.currentDirection:
            case Directions.STOP:
                motorDriver.set_idle_mode()
            case Directions.FORWARD:
                motorDriver.set_forward_mode()
            case Directions.BACKWARD:
                motorDriver.set_reverse_mode()

    def run(self):
        self.get_direction()
        time.sleep(0.1)


class CameraManager:
    def __int__(self):
        self.cam = cv.VideoCapture(0)

    def get_image(self):
        # reading the input using the camera
        result, image = self.cam.read()
        # If image will be detected without any error, shows result
        if result:
            name = str(time.time())
            # showing result, it takes frame name and image output
            cv.imshow(name, image)
            # saving image in local storage
            cv.imwrite(name + ".png", image)
            # If keyboard interrupt occurs, destroy image window
            cv.waitKey(0)
            cv.destroyWindow(name)
            return image
        # If captured image is corrupted, moving to else part
        else:
            print("No image detected. Please! try again")
            return None

    def upload_image(self):
        """Upload camera image to the website"""
        image = self.get_image()
        files = {
            'file': ("frame", open('/usr/tmp', 'rb')),
            'Content-Type': 'image/jpeg',
            'Content-Length': 1
        }
        request = requests.post('https://w3schools.com/python/demopage.htm', files=files)

    def run(self):
        self.upload_image()
        time.sleep(0.1)


if __name__ == '__main__':
    # Create objects
    car_os = RCcarOS
    cam_mngr = CameraManager
    # Create threads
    car_os_thread = threading.Thread(target=car_os.run)
    car_move_thread = threading.Thread(target=car_os.move_car)
    cam_mngr_thread = threading.Thread(target=cam_mngr.run)
    # Start the threads
    car_os_thread.start()
    car_move_thread.start()
    cam_mngr_thread.start()
    # Join the threads
    # car_os_thread.join()
    # car_move_thread.join()
    # cam_mngr_thread.join()
