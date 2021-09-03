#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


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

# OBJECTS
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
front_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, 140)
robot.settings(200, 100, 150, 100)
gyro = GyroSensor(Port.S4)

# PROGRAM
two_inches = inches_to_mm(2)
robot.straight(two_inches)
robot.turn(90)
robot.straight(two_inches)

#This is a change
#This is another change