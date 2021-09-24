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


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=121)
light = ColorSensor(Port.S1)

# Write your program here.
while robot.distance() >= 1000:
    correction = (30 - light.reflection())*2
    robot.drive(100,correction)
robot.stop()
left_motor.brake()
right_motor.brake()