from pyfirmata import Arduino, util
import time
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

port = 'COM5'  # Puerto donde está conectado el Arduino
board = Arduino(port)

it = util.Iterator(board)
it.start()

time.sleep(2)

rs = board.get_pin('d:7:o')  # Pin de control RS
en = board.get_pin('d:8:o')  # Pin de control Enable
d4 = board.get_pin('d:9:o')  # Pin de datos D4
d5 = board.get_pin('d:10:o')  # Pin de datos D5
d6 = board.get_pin('d:11:o')  # Pin de datos D6
d7 = board.get_pin('d:12:o')  # Pin de datos D7

# Establecer los pines de datos en modo de salida
rs.mode = board.OUTPUT
en.mode = board.OUTPUT
d4.mode = board.OUTPUT
d5.mode = board.OUTPUT
d6.mode = board.OUTPUT
d7.mode = board.OUTPUT

def lcd_command(data):
    rs.write(0)  # RS LOW for command mode

    d4.write(data & 0x10)
    d5.write(data & 0x20)
    d6.write(data & 0x40)
    d7.write(data & 0x80)

    en.write(1)
    time.sleep(0.01)
    en.write(0)
    time.sleep(0.01)

def lcd_init():
    time.sleep(0.02)  # Retardo inicial

    lcd_command(0x03)  # Inicialización
    time.sleep(0.005)
    lcd_command(0x03)  # Inicialización
    time.sleep(0.001)
    lcd_command(0x03)  # Inicialización
    time.sleep(0.001)
    lcd_command(0x02)  # Modo de 4 bits
    time.sleep(0.001)
    lcd_command(0x02)  # Modo de 4 bits
    time.sleep(0.001)
    lcd_command(0x08)  # Modo de 4 bits, 2 líneas, fuente 5x7
    time.sleep(0.001)
    lcd_command(0x00)  # Limpiar la pantalla
    time.sleep(0.001)
    lcd_command(0x0C)  # Encender el LCD
    time.sleep(0.001)
    lcd_command(0x06)  # Incrementar cursor
    time.sleep(0.001)

def lcd_text(text):
    for char in text:
        lcd_command(ord(char))

try:
    lcd_init()  # Inicialización del LCD
    lcd_text("Hola, mundo!")  # Mostrar texto
    time.sleep(3)
    lcd_command(0x01)  # Limpiar la pantalla
    time.sleep(1)

except KeyboardInterrupt:
    lcd_command(0x01)  # Limpiar la pantalla antes de terminar
    board.exit()