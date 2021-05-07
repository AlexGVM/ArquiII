import RPi.GPIO as GPIO
import requests
import time


URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
URL = URL + "?pulso=r" + "0110"
response = requests.get(URL)
      
URL = 'https://w95davn4k4.execute-api.us-east-2.amazonaws.com/Fase1/'
URL = URL + "?pulso=" + str(1)
response1 = requests.get(URL)
print(response1.text)
