import requests
import RPi.GPIO as GPIO
import time
from datetime import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT) #0
GPIO.setup(11,GPIO.OUT) #1
GPIO.setup(5,GPIO.OUT) #2
GPIO.setup(6,GPIO.OUT) #3
GPIO.setup(13,GPIO.OUT) #4
GPIO.setup(19,GPIO.OUT) #5
GPIO.setup(2,GPIO.OUT) #5
GPIO.setup(26,GPIO.OUT) #6

GPIO.setup(20,GPIO.IN) #dip
time1 = 0
while True:
    if GPIO.input(20):
        time1 = 1
        URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
        URL = URL + "?PulsoPi=" + str(time1)
        response = requests.post(URL)
        print(response.status_code)
        bit1 = response.text[1]
        bit2 = response.text[2]
        bit3 = response.text[3]
        bit4 = response.text[4]
        bit5 = response.text[5]
        bit6 = response.text[6]
        bit7 = response.text[7]
        bit8 = response.text[8]
        
        if bit1 == "1" or bit1 == "0":
            if bit1 == "1":
                GPIO.output(9,True)
            else:
                GPIO.output(9, False)
                
        if bit2 == "1" or bit2 == "0":
            if bit2 == "1":
                GPIO.output(11,True)
            else:
                GPIO.output(11, False)
        
        if bit3 == "1" or bit3 == "0":
            if bit3 == "1":
                GPIO.output(5,True)
            else:
                GPIO.output(5, False)
                
        if bit4 == "1" or bit4 == "0":
            if bit4 == "1":
                GPIO.output(6,True)
            else:
                GPIO.output(6, False)
                
        if bit5 == "1" or bit5 == "0":
            if bit5== "1":
                GPIO.output(13,True)
            else:
                GPIO.output(13, False)
                
        if bit6 == "1" or bit6 == "0":
            if bit6 == "1":
                GPIO.output(19,True)
            else:
                GPIO.output(19, False)
                
        if bit7 == "1" or bit7 == "0":
            if bit7 == "1":
                GPIO.output(26,True)
            else:
                GPIO.output(26, False)
             
                
        if bit8 == "1" or bit8 == "0":
            if bit8 == "1":
                GPIO.output(2,True)
            else:
                GPIO.output(2,False)
        print(response.text)
        
    else:
        time1 = 0
        URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
        URL = URL + "?PulsoPi=" + str(time1)
        response = requests.post(URL)
        print(response.status_code)
        bit1 = response.text[1]
        bit2 = response.text[2]
        bit3 = response.text[3]
        bit4 = response.text[4]
        bit5 = response.text[5]
        bit6 = response.text[6]
        bit7 = response.text[7]
        
        if bit1 == "1" or bit1 == "0":
            if bit1 == "1":
                GPIO.output(9,True)
            else:
                GPIO.output(9, False)
                
        if bit2 == "1" or bit2 == "0":
            if bit2 == "1":
                GPIO.output(11,True)
            else:
                GPIO.output(11, False)
        
        if bit3 == "1" or bit3 == "0":
            if bit3 == "1":
                GPIO.output(5,True)
            else:
                GPIO.output(5, False)
                
        if bit4 == "1" or bit4 == "0":
            if bit4 == "1":
                GPIO.output(6,True)
            else:
                GPIO.output(6, False)
                
        if bit5 == "1" or bit5 == "0":
            if bit5 == "1":
                GPIO.output(13,True)
            else:
                GPIO.output(13, False)
                
        if bit6 == "1" or bit6 == "0":
            if bit6 == "1":
                GPIO.output(19,True)
            else:
                GPIO.output(19, False)
                
        if bit7 == "1" or bit7 == "0":
            if bit7 == "1":
                GPIO.output(26,True)
                GPIO.output(2,True)
            else:
                GPIO.output(26, False)
                GPIO.output(2,False)
    
GPIO.cleanup()
        

        
        
        
        
   
        
    
        
        
   
    
    




