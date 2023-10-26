import pyfirmata
import time
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

board = pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[2].mode = pyfirmata.INPUT

while True:
    sw = board.digital[2].read()
    
    if sw is False:
        board.digital[7].write(1)
        
    else:
        board.digital[7].write(0)
        
    time.sleep(0.1)
    