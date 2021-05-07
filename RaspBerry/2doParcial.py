from datetime import datetime
import time
from os import system
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT) # este pin es de salida carro
GPIO.setup(26, GPIO.OUT) # este pin es de salida carro
GPIO.setup(19, GPIO.OUT) # este pin es de salida carro
GPIO.setup(13, GPIO.OUT) # este pin es de salida carro
GPIO.setup(6, GPIO.OUT) # este pin es de salida carro
GPIO.setup(5, GPIO.OUT) # este pin es de salida carro
GPIO.setup(11, GPIO.OUT) # este pin es de salida carro
GPIO.setup(20, GPIO.IN) #Este pin es una entrada carro pequeno
GPIO.setup(16, GPIO.IN) #Este pin es una entrada carro grande


PATH_CRED = '/home/pi/Desktop/cred.json'
URL_DB = 'https://arquiii-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(PATH_CRED)
firebase_admin.initialize_app(cred, {
    'databaseURL': URL_DB
})
REF = db.reference("/")

REF.set({
    'Proceso': 
    {
    }
})

REF = db.reference("/Vehiculos")

while True:
    tiempo = datetime.now()
    #Si hay un 1 en el pin 20
    if GPIO.input(20):
        tiempoE = 5 #tiempo que va a cambiar por estacion
        if GPIO.input(20):
            tamano = "Pequeno"
        elif GPIO.input(20) and GPIO.input(16):
            tamano = "Grande"
        else:
            tamano = "Mediano"
        
        print("Se ha detectado un automovil de tamano",tamano)
        REF.push({        
                    "Recepcion": str(tiempo),
                    "Tamano": tamano,     
                    })
        if (tiempo == 5):
            print("Activacion de agua... ")
            tiempo += 5
            GPIO.output(26, True)
            print("Desactivacion de agua...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo agua": str(tiempo),    
                    })
            GPIO.output(26, False)
        elif (tiempo == 10):
            print("Activacion de rocio de shampoo... ")
            tiempo += 5
            GPIO.output(19, True)
            print("Desactivacion de rocio de shampoo...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo rocio": str(tiempo),    
                    })
            GPIO.output(19, False)
        elif (tiempo == 15):
            print("Activacion de rodillos de limpieza... ")
            tiempo += 5
            GPIO.output(13, True)
            print("Desactivacion de rodillos de limpieza...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo rodillo": str(tiempo),    
                    })
            GPIO.output(13, False)
        elif (tiempo == 20):
            print("Activacion de escobas de limpieza ")
            tiempo += 5
            GPIO.output(6, True)
            print("Desactivacion de escobas de limpieza...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo escoba": str(tiempo),    
                    })
            GPIO.output(6, False)
        elif (tiempo == 25):
            print("Activacion de rocio de agua 2nda vez ")
            tiempo += 5
            GPIO.output(5, True)
            print("Desactivacion de rocio de agua 2nda vez...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo agua 2nda": str(tiempo),    
                    })
            GPIO.output(5, False)
        elif (tiempo == 30):
            print("Activacion de rodillos de secado")
            tiempo += 5
            GPIO.output(11, True)
            print("Desactivacion de rodillos de secado...")
            tiempo = datetime.now()
            REF.push({        
                    "Tiempo rodillos": str(tiempo),    
                    })
            GPIO.output(11, False)
        
GPIO.cleanup()




