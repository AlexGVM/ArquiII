from datetime import datetime
import time
from os import system
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT) # este pin es de salida
GPIO.setup(20, GPIO.IN) #Este pin es una entrada.
GPIO.setup(16, GPIO.IN)

while True:
    tiempo = datetime.now()
    #Si hay un 1 en el pin 20
    if GPIO.input(20):
        GPIO.output(21, False)
        print("Se ha detectado una continuidad de sensor a las",str(tiempo))
        while GPIO.input(20):
            tiempo = datetime.now()
        
    else:
        GPIO.output(21, True)
        print("Se ha detectado una interrupcion de sensor a las",str(tiempo))
        while not GPIO.input(20):
            tiempo = datetime.now()
       
GPIO.cleanup()