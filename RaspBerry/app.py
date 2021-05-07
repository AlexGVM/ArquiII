from flask import Flask
import time

app = Flask(__name__)

@app.route('/')


def main():    
    lista = list()
    while True:
        contador = 0
        if contador == 0:
            contador = 1
            time.sleep(2)
            texto = 'el contador es 0'
            lista.append(texto)
        if contador == 1:
            time.sleep(2)
            texto = 'el contador es 1'
            lista.append(texto)
        dato = str(lista)
        index()
        
def index():
    return dato
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')