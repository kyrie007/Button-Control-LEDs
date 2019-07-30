#!/usr/bin/python
# Assignment 4#

###  import Python Modules  ###
import threading
import RPi.GPIO as GPIO
import time


###  Set GPIO pins and all setups needed  ###
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)#btn_red
GPIO.setup(27,GPIO.IN)#btn_yellow
GPIO.setup(22,GPIO.IN)#btn_blue
GPIO.setup(25,GPIO.IN)#btn_green
GPIO.setup(12,GPIO.OUT)#led_yellow
GPIO.setup(5,GPIO.OUT)#led_green
GPIO.setup(6,GPIO.OUT)#led_red
GPIO.setup(13,GPIO.OUT)#led_blue

### Define a function based on assignment description  ###
def blink():
    GPIO.output(6,False)#light red led
    GPIO.output(5,False)#light greeb led
    time.sleep(0.2)
    GPIO.output(6,True)#dark red led 
    GPIO.output(5,True)#dark green led
    time.sleep(0.2)
    
    
if __name__ == "__main__":
    next_step=False
    GPIO.output(13,True)	#make yellow led dark
    GPIO.output(12,True)	#make blue led dark
    GPIO.output(6,True)		#make red led dark
    GPIO.output(5,True)		#make green led dark
    while(True):
        if GPIO.input(27):	 #check if yellow button is clicked
            cnt=10
            while(True):
                if GPIO.input(18) and GPIO.input(25):	#check if red and green button are clicked. If clicked, then set true
                    next_step=True 
                if next_step: 
                    blink()
                    cnt-=1
                    if cnt<0: #if blink ten times then stop act like a certain time
                        next_step=False
                        GPIO.output(6,True) #dark red led
                        GPIO.output(5,True) #dark green led
                        break
                if GPIO.input(22):	#checki if blue button is clicked
                    next_step=False
                    GPIO.output(6,True) #dark red led
                    GPIO.output(5,True) #dark green led
                    break
        elif GPIO.input(22):	#same as the one above but replace yellow with blue button
            cnt=10
            while(True):
                if GPIO.input(18) and GPIO.input(25):  
                    next_step=True
                if next_step:
                    blink()
                    cnt-=1
                    if cnt<0:
                        next_step=False
                        GPIO.output(6,True)
                        GPIO.output(5,True)
                        break
                if GPIO.input(27):	
                    next_step=False
                    GPIO.output(6,True)
                    GPIO.output(5,True)
                    break
GPIO.clearup()