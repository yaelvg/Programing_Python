import pyfirmata
import time
import inspect
import random as rand

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

board = pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

''''
Leds
azul = 5
rojo = 6
verde = 7
amarillo = 8
'''
#Nivel inicial
nivel= 1



# INICIALIZAR Botones
#AZUL
board.digital[2].mode = pyfirmata.INPUT
#Rojo
board.digital[3].mode = pyfirmata.INPUT
#Verde
board.digital[4].mode = pyfirmata.INPUT
#Amarillo
board.digital[5].mode = pyfirmata.INPUT




while True:
    
    bt1= board.digital[2].read()
    bt2= board.digital[3].read()
    bt3= board.digital[4].read()
    bt4= board.digital[5].read()
    
    if bt1 is False:
        board.digital[7].write(1)
        
    else:
        board.digital[7].write(0)
        
    time.sleep(0.1)


def generar(nivel):
    #Necesito 4 numeros que sean los pines digital de los led y se almacenen
    for i in range(nivel):
        lista()
        pin = rand.randint(2,3,4,5)
        lista.append(pin)
    return lista

def mostrar_secuencia(secuencia):
    #Muestra en los leds como es el funcionamiento de la secuencia
    for i in range(len(secuencia)):
        board.digital[i].write(1)