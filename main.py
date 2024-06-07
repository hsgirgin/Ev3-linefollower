#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



hsg = EV3Brick()
eyes = UltrasonicSensor(Port.S3)
right = ColorSensor(Port.S2)
left = ColorSensor(Port.S1)
mid = ColorSensor(Port.S4)
rmotor = Motor(Port.A,positive_direction=Direction.CLOCKWISE,gears=[40,40,40])
lmotor = Motor(Port.D,positive_direction=Direction.CLOCKWISE,gears=[40,40,40])
# Functions
def check_line():
        
        check1 = False

        # First check: <--2s
        time_start = time.time()
        while time.time() < time_start + 2 :
            print(time.time() - time_start)
            lmotor.run(-50)
            rmotor.run(50)
            if mid.reflection() <= 15 or right.reflection() <= 15 :
                check1 = True
                break

        # Second check: -->4s
        time_start = time.time()
        while time.time() < time_start + 4 and check1 == False:
            lmotor.run(50)
            rmotor.run(-50)
            if mid.reflection() <= 15 or left.reflection() <= 15 :
                check1 = True
                break

        # Third check: <--2s
        time_start = time.time()
        while time.time() < time_start + 2 and check1 == False:
            lmotor.run(-50)
            rmotor.run(50)
            if mid.reflection() <= 15 or right.reflection() <= 15:
                check1 = True
                break
        

        return check1
def rturn():
    mstop(100)
    angle = lmotor.angle()
    while angle + 210 > lmotor.angle():
        print(lmotor.angle())
        lmotor.run(200)
        rmotor.run(-200)
def lturn():
    mstop(100)
    angle = rmotor.angle()
    while angle + 210 > rmotor.angle():
        print(rmotor.angle())
        lmotor.run(-200)
        rmotor.run(200)   
def mstop(time):
    rmotor.hold()
    lmotor.hold()
    wait(time)
def back(time):
    mstop(200)
    if int(time)==0:
        lmotor.run(-190)
        rmotor.run(-190) 
    else:
        lmotor.run(-190)
        rmotor.run(-190)
        wait(time)
def forward(time):
    if int(time)==0:
        lmotor.run(150)
        rmotor.run(150) 
    else:
        lmotor.run(200)
        rmotor.run(200)
        wait(time)
def turn(time,side):
    mstop(200)
    if side == "r":
        if int(time)==0:
            lmotor.run(200)
            rmotor.run(-200)
        else:
            lmotor.run(200)
            rmotor.run(-200)
            wait(time)
    else:
        if int(time)==0:
            lmotor.run(-200)
            rmotor.run(200) 
        else:
            lmotor.run(-200)
            rmotor.run(200)
            wait(time)
def room():
    # Find first wall
    time_start = time.time()
    while eyes.distance() > 40:
        lmotor.run(200)
        rmotor.run(200) 
        time_end = time.time()
        if right.reflection() <= 20 or mid.reflection() <= 20 or left.reflection() <= 20:
            return
    time_mid = time_end - time_start
    time_start = time.time()
    while time.time() < time_start + time_mid:
        lmotor.run(-100)
        rmotor.run(-100) 
    lturn()
    time_start = time.time()
    while eyes.distance() > 40:
        lmotor.run(200)
        rmotor.run(200) 
        time_end = time.time()
        if right.reflection() <= 20 or mid.reflection() <= 20 or left.reflection() <= 20:
            return
    time_start = time_end - time_start
    while time.time() < time_start:
        lmotor.run(-100)
        rmotor.run(-100) 
        
    rturn()
    rturn()
    time_start = time.time()
    while eyes.distance() > 40:
        lmotor.run(200)
        rmotor.run(200) 
        time_end = time.time()
        if right.reflection() <= 20 or mid.reflection() <= 20 or left.reflection() <= 20:
            return
    

    '''
    # Check if wall left/right
    ltr = 0
    rturn()
    if eyes.distance() < 40:
        lturn()
    else:
        lturn()
        ltr = 1

    # Main room program
    while right.reflection() >= 20 and mid.reflection() >= 20 and left.reflection() >= 20:

        # Turn side according to wall
        if ltr:
            rturn()
        else:    
            lturn()

        # 4s distance/found line
        time_start = time.time()
        while time.time() < time_start + 4 and eyes.distance() > 40:
            forward(0)
        while eyes.distance() > 60:
            forward(50)

        # Orientation
        while eyes.distance() < 50:
            back(200)
        # Turn to wall(normal)
        if time.time() > time_start + 4:
            if check_line() == True:
                    break
            if ltr:
                lturn()
            else:
                rturn()
            
        
        # Less than 4s: Wall found
        else:
            
            

            # Check for wall before changing side    
            if ltr:
                lturn()
            else:    
                rturn()
            
            # No wall
            if eyes.distance() > 100:
               forward(200) 
            
            # Wall: change side
            else:
                if ltr:
                    rturn()
                else:    
                    lturn()
    '''
            
        


amount = 0
while True:
    '''if eyes.distance() < 100:
        
        rturn()
        forward(1800)
        lturn()
        forward(5500)
        lturn()
        forward(1800)
        rturn()
        back(2000)'''

    # Silver
    if right.reflection() >= 90 or mid.reflection() >= 90 or left.reflection() >= 90:
        room()

    #  Mid
    elif right.reflection() >= 20 and mid.reflection() <= 20 and left.reflection() >= 20:
        forward(20)

    # All
    elif right.reflection() <= 20 and mid.reflection() <= 20 and left.reflection() <= 20:
        mstop(0)

        #Green
        if left.color() == Color.GREEN or right.color() == Color.GREEN or mid.color() == Color.GREEN:
            print("3")
            forward(700)
            lturn()
            lturn()
            back(100)
        elif left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        #Black
        else:
            forward(600)
        mstop(100)

    # Mid and Left    
    elif right.reflection() >= 20 and mid.reflection() <= 20 and left.reflection() <= 20:
        mstop(0)
        forward(50)
        # Green
        if left.color() == Color.GREEN and right.color() == Color.GREEN:
            forward(700)
            lturn()
            lturn()
            back(50)
        elif left.color() == Color.GREEN:
            print("3")
            forward(700)
            lturn()
            forward(50)

        # Black
        elif left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        elif left.color() == None or mid.color() == None:
            forward(100)
        else:
            forward(100)
            mstop(100)
            if mid.color() != Color.WHITE or right.color() != Color.WHITE or left.color() != Color.WHITE:
                forward(250)
            else:
                forward(400)
                lturn()
                back(200)
        mstop(100)

    # Mid and Right 
    elif right.reflection() <= 20 and mid.reflection() <= 20 and left.reflection() >= 20:
        mstop(0)
        forward(50)
        # Green
        if left.color() == Color.GREEN and right.color() == Color.GREEN:
            forward(700)
            lturn()
            lturn()
            back(50)
        elif right.color() == Color.GREEN:
            print("3")
            forward(700)
            rturn()
            forward(50)
        elif left.color() == None or right.color() == None:
            forward(100)
        elif left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        # Black
        else:
            forward(100)
            mstop(100)
            if mid.color() != Color.WHITE or right.color() != Color.WHITE or left.color() != Color.WHITE:
                forward(250)
            else:
                forward(400)
                rturn() 
                back(200)
        mstop(100)
        
    # Right
    elif right.reflection() <= 20 and mid.reflection() >= 20 and left.reflection() >= 20:
        print("5")
        print('r')
        print(right.color(),left.color())
        mstop(50)
        if right.color() == None:
            forward(100)
            mstop(100)
        elif left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        else:
            mstop(100)
            time_start = time.time()
            while mid.reflection() >= 20 and time.time() < time_start + 6:
                lmotor.run(50)
                rmotor.run(-50)
            if time.time() > time_start + 6:
                time_start = time.time()
                while mid.reflection() >= 20 and time.time() < time_start + 6:
                    lmotor.run(-50)
                    rmotor.run(50)
                forward(200)

    # Left	
    elif right.reflection() >= 20 and mid.reflection() >= 20 and left.reflection() <= 20:
        print("6")
        print('l')
        mstop(0)
        if left.color() == None or right.color() == None:
            forward(100)
            mstop(0)
        elif left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        else:
            mstop(100)
            time_start = time.time()
            while mid.reflection() >= 20 and time.time() < time_start + 6:
                lmotor.run(-50)
                rmotor.run(50)
            if time.time() > time_start + 6:
                time_start = time.time()
                while mid.reflection() >= 20 and time.time() < time_start + 6:
                    lmotor.run(50)
                    rmotor.run(-50)
                forward(200)

    # All White
    elif right.reflection() >= 20 and mid.reflection() >= 20 and left.reflection() >= 20:
        print("7")
        
        if left.color() == Color.RED or right.color() == Color.RED or mid.color() == Color.RED:
            exit()
        mstop(50)
        if right.reflection() >= 90 and mid.reflection() >= 90 and left.reflection() >= 90:
            amount = 0
        check = False
        time_start = time.time()
        while time.time() < time_start + 2 :
            print(time.time() - time_start)
            lmotor.run(-50)
            rmotor.run(50)
            if mid.reflection() <= 15 or right.reflection() <= 15 :
                check = True
                amount = 0
                break
        time_start = time.time()
        while time.time() < time_start + 4 and check == False:
            lmotor.run(50)
            rmotor.run(-50)
            if mid.reflection() <= 15 or left.reflection() <= 15 :
                check = True
                amount = 0
                break
        time_start = time.time()
        while time.time() < time_start + 2 and check == False:
            lmotor.run(-50)
            rmotor.run(50)
            if mid.reflection() <= 15 or right.reflection() <= 15:
                check = True
                amount = 0
                break
        if check != True:
            if amount < 3:
                amount = amount + 1
                forward(600)
            else:
                amount = 0
                back(800)
                room()
