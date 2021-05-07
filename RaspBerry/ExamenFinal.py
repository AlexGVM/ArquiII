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


numerosD = []

while True:
    
    URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
    URL = URL + "?pulso=" + str(1)
    time.sleep(3)
    response = requests.get(URL)
    numero = response.text[3]
    print(numero)
    
    if numero == "1":
        GPIO.output(2,True) #punto
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        
    if numero == "2":
        
        GPIO.output(2,True) #punto1
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto2
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        
    if numero == "3":
        
        GPIO.output(2,True) #punto1
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto2
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto3
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        
    if numero == "4":
        
        GPIO.output(2,True) #punto1
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto2
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto3
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto4
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        
    if numero == "5":
        
        GPIO.output(2,True) #punto1
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto2
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto3
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto4
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto5
        time.sleep(1)
        GPIO.output(2,False)
        
    if numero == "6":
        
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto2
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto3
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto4
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto5
        time.sleep(1)
        GPIO.output(2,False)
    
    if numero == "7":
        
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto3
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto4
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto5
        time.sleep(1)
        GPIO.output(2,False)
        
    if numero == "8":
        
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto4
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto5
        time.sleep(1)
        GPIO.output(2,False)
        
    if numero == "9":
        
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #punto5
        time.sleep(1)
        GPIO.output(2,False)
        
    if numero == "0":
        
        GPIO.output(2,True) #barra1
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra2
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra3
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra4
        time.sleep(3)
        GPIO.output(2,False)
        time.sleep(1)
        GPIO.output(2,True) #barra5
        time.sleep(3)
        GPIO.output(2,False)
        
        
GPIO.cleanup()
