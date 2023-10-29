from pyfirmata import Arduino, util
import time
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

# Puerto donde está conectado el Arduino
port = 'COM6'  # Cambia esto al puerto correspondiente en tu sistema

board = Arduino(port)

# Espera a que se establezca la conexión
while not board:
    pass

# Inicialización de la comunicación
it = util.Iterator(board)
it.start()

# Esperar un tiempo para establecer la conexión
time.sleep(2)

# Función para enviar texto a la pantalla LCD
def send_to_lcd(text):
    board.send_sysex(0x71, bytearray(text.encode()))

# Mensaje a enviar a la pantalla LCD
message = "Hola desde Python"

try:
    while True:
        send_to_lcd(message)
        time.sleep(2)
        board.send_sysex(0x71, bytearray("clear".encode()))  # Comando para limpiar la pantalla
        time.sleep(2)

except KeyboardInterrupt:
    board.send_sysex(0x71, bytearray("clear".encode()))  # Limpiar la pantalla antes de terminar
    board.exit()