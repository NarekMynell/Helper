import cv2 as cv
from djitellopy import tello


drone = tello.Tello()
drone.connect()

drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv.resize
