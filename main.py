#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
WHEEL_DIAMETER = 56

# FUNCTIONS HERE
def inches_to_mm(inches):
    return inches * 25.4

def sec_to_ms(seconds):
    MS = 1000
    return seconds * MS

def robot_stop():
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    wait(seconds(0.25))

'''def straight_left_straight(distance1, angle, distance2):
    robot.straight(inches_to_mm(distance1))
    random.randint(sec_to_ms(1), sec_to_ms(10))
    robot.turn(angle)
    random.randint(sec_to_ms(1), sec_to_ms(10))
    robot.straight(inches_to_mm(distance2))'''
    
def straight_to_the_top(wait_time1, wait_time2):
    gyro.reset_angle(0)

    angle = gyro.angle()

    wait(wait_time1)


    while robot.distance() < 1000:
        angle = gyro.angle()
        print(angle)
        robot.drive(100, angle * -1)

#def gyro_turn(turn_angle):



# OBJECTS
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
front_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, 140)
#robot.settings(200, 100, 150, 100)
gyro = GyroSensor(Port.S4)

# PROGRAM
straight_to_the_top(3000,3000)


#This is a change
#This is another change

