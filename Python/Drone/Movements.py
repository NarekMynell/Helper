import cv2 as cv
from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

drone.takeoff()
drone.send_rc_control(0, 25, 0, 0)
sleep(4)
drone.send_rc_control(0, 0, 0, 0)
drone.land()

