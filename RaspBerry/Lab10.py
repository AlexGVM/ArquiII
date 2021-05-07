import RPi.GPIO as GPIO
import requests
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT) #0
GPIO.setup(11,GPIO.OUT) #1
GPIO.setup(5,GPIO.OUT) #2
GPIO.setup(6,GPIO.OUT) #3
GPIO.setup(13,GPIO.OUT) #4
GPIO.setup(19,GPIO.OUT) #5
GPIO.setup(2,GPIO.OUT) #6
GPIO.setup(8,GPIO.OUT)
GPIO.setup(26,GPIO.OUT) #led

GPIO.setup(20,GPIO.IN) #dip bit0
GPIO.setup(16,GPIO.IN) #dip bit1
GPIO.setup(12,GPIO.IN) #dip bit2
GPIO.setup(7,GPIO.IN) #dip bit3
GPIO.setup(18,GPIO.IN) #dip mandar mensaje bit

GPIO.output(26,True)
time.sleep(1)
GPIO.output(26,False)

def binarioDecimal(binario):
    if binario == "11111100":
        return 0
    if binario == "01100000":
        return 1
    if binario == "11011010":
        return 2
    if binario == "11110010":
        return 3
    if binario == "01100110":
        return 4
    if binario == "10110110":
        return 5
    if binario == "10111110":
        return 6
    if binario == "11100000":
        return 7
    if binario == "11111110":
        return 8
    if binario == "11110110":
        return 9
    if binario == "11111101":
        return 10
    if binario == "01100001":
        return 11
    if binario == "11011011":
        return 12
    if binario == "11110011":
        return 13
    if binario == "01100111":
        return 14
    if binario == "10110111":
        return 15
    
while True:
    binario = ""
    contador = 1
    display = ""
    while GPIO.input(18):
        if GPIO.input(20): #si es uno
            binario = binario + "1"
        else:
            binario = binario + "0"
            
        if GPIO.input(16): #si es uno
            binario = binario + "1"
        else:
            binario = binario + "0"
            
        if GPIO.input(12): #si es uno
            binario = binario + "1"
        else:
            binario = binario + "0"
            
        if GPIO.input(7): #si es uno
            binario = binario + "1"
        else:
            binario = binario + "0"
            
        URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
        URL = URL + "?pulso=r" + str(binario)
        response = requests.get(URL)
        time.sleep(7)
        URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
        URL = URL + "?pulso=" + str(1)
        response = requests.get(URL)
        
        bit0 = response.text[3]
        bit1 = response.text[4]
        bit2 = response.text[5]
        bit3 = response.text[6]
        bit4 = response.text[7]
        bit5 = response.text[8]
        bit6 = response.text[9]
        bit7 = response.text[10]
        
        if bit0 == "1" or bit0 == "0":
            if bit0 == "1":
                GPIO.output(9,True)
            else:
                GPIO.output(9, False)
                
        if bit1 == "1" or bit1 == "0":
            if bit1 == "1":
                GPIO.output(11,True)
            else:
                GPIO.output(11, False)
        
        if bit2 == "1" or bit2 == "0":
            if bit2 == "1":
                GPIO.output(5,True)
            else:
                GPIO.output(5, False)
                
        if bit3 == "1" or bit3 == "0":
            if bit3 == "1":
                GPIO.output(6,True)
            else:
                GPIO.output(6, False)
                
        if bit4 == "1" or bit4 == "0":
            if bit4 == "1":
                GPIO.output(13,True)
            else:
                GPIO.output(13, False)
                
        if bit5 == "1" or bit5 == "0":
            if bit5 == "1":
                GPIO.output(19,True)
            else:
                GPIO.output(19, False)
                
        if bit6 == "1" or bit6 == "0":
            if bit6 == "1":
                GPIO.output(2,True)
            else:
                GPIO.output(2, False)
                
        if bit7 == "1" or bit7 == "0":
            if bit7 == "1":
                GPIO.output(26,True)
            else:
                GPIO.output(26, False)
                
        display = bit0 + bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7
        numeroDecimal = binarioDecimal(display)
        
        while contador <= numeroDecimal:
            GPIO.output(8,True)
            time.sleep(1)
            GPIO.output(8,False)
            time.sleep(1)
            contador += 1
            
    

    
GPIO.cleanup()


