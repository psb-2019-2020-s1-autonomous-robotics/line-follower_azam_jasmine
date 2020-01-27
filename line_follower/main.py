#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.beep()

    
test_motor1 = Motor(Port.C, Direction.CLOCKWISE)
test_motor2 = Motor(Port.A, Direction.CLOCKWISE)
robot = DriveBase(test_motor1, test_motor2, 35, 114)

Tsensor = TouchSensor(Port.S1)
Csensor = ColorSensor(Port.S2)
Csensor.mode = 'RGB-RAW'

while not Tsensor.pressed():
    wait(10)

while True: 

#Works when background is pure white and line is blue
#Otherwise: must change threshold values for color[0], color[1], and/or color[2]

    color = Csensor.rgb()
    print(color) 

    #Line
    while color[0] <= 15 and color[1] <= 15:
        wait(1)
        robot.drive(100, 0)
        color = Csensor.rgb()
        print(color) 

    #Not line
    while color[0] > 15 and color[1] > 15: 
        robot.stop()
        wait(100)
        #Turning clockwise?
        i = 0
        rep = 90
        while i < rep:
            wait(1)
            robot.drive_time(10, 15, 100)
            color = Csensor.rgb()
            print(color)
            if color[0] <= 15 and color[1] <= 15:
                break
            i += 1
        #Turning counterclockwise
        robot.stop()
        rep = 140
        i = 0
        while i < rep:
            wait(1)
            robot.drive_time(305, -25, 100)
            color = Csensor.rgb()
            print(color)
            if color[0] <= 15 and color[1] <= 15:
                break
            i+=1
        
   
brick.sound.beep(1000, 500)

