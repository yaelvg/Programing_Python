import pyfirmata
import time
import inspect
import random as rand

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


board = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(board)
it.start()

led = board.get_pin('d:13:o')
bton= board.get_pin('d:2:i' )

while True:
    
    estado = bton.read()
        
    if estado == 1:
        led.write(1)
    else:
        led.write(0)