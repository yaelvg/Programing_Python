#Este es un cambio hecho desde github ;)
from pyfirmata import Arduino, util
import time
import inspect
import random as rand

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

BUZZER_PIN = 10  # Ajusta el número de pin al que está conectado el buzzer

melodia_error = [262, 196, 196, 220, 196, 1000, 247, 262]

melodia_x=[262, 262,196, 196 ]

melodia_bienvenida = [415.30, 392, 369.99, 349.23, 329.63, 311.13, 293.66, 277.18, 261.63]

duracionNotas = [4000, 8000, 8000, 4000, 4000, 4000, 4000, 4000]

duracionNotas_2 = [3000, 7000, 3000, 5000, 3000, 2000, 9000, 2000]


board = Arduino('COM6')  # Cambia 'COM3' por tu puerto
buzzer = board.get_pin('d:10:p' )

it = util.Iterator(board)
it.start()
#Melodia error
def error():
    for i in range(8):
        duracionNota = 1000/duracionNotas_2[i]
        buzzer.write(1000/melodia_error[i])
        time.sleep(duracionNota)
        pausaEntreNotas = duracionNota * 1.30
        buzzer.write(0)
        time.sleep(pausaEntreNotas)

def bienvenida():
    for i in range(8):
        duracionNota = 1000/duracionNotas[i]
        buzzer.write(1000/melodia_error[i])
        time.sleep(duracionNota)
        pausaEntreNotas = duracionNota * 1.30
        buzzer.write(0)
        time.sleep(pausaEntreNotas) 
        
def paso_nivel():
    for i in range(4):
        buzzer.write(1000/melodia_error[i])
        time.sleep(1/10)
        pausaEntreNotas = 1/10 * 1.30
        buzzer.write(0)
        time.sleep(pausaEntreNotas)
def pusheo():
    buzzer.write(1)
    time.sleep(1/10)
    buzzer.write(0) 
    
