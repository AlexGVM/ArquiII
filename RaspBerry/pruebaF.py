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

numerosD = []

while True:
    
    URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
    URL = URL + "?pulso=" + str(1)
    response = requests.get(URL)
    numero = response.text
    print(numero)

    
    
        
        
GPIO.cleanup()

