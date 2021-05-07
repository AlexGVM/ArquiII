import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT) # este pin es de salida

while True:
    print("Izquierdo")
    GPIO.output(21, True)
    time.sleep(2)
    print("Derecho")
    GPIO.output(21, False)
    time.sleep(2)
GPIO.cleanup()