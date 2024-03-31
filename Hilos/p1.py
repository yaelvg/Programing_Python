
#* Librerias importantes para el uso de hilos, agregando time y datetime
import threading
import time
import datetime
import logging #! Podemos mandar un mensaje de información para ver lo que pasa

# * INF indica el nivel de información que vamos a obtener
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def consultar(id_persona):
    logging.info('Consulta del hilo para el id:' + str(id_persona))
    time.sleep(2)
    return

def guardar(id_persona, data):
    logging.info('Consulta del hilo para el id:' + str(id_persona) + 'y data ' + str(data))
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()
# * Al usar estas dos funciones sin hilos el tiempo de ejecucion es ovbiamente lente
#* consultar(1)

#* guardar(1, 'hola sin uso de hilos')

# ? Al usar estos dos hilos y unirlos hacemos que inmediatamente cuando el primer hilo de 2 seg se inicia
# ? el de 5 de igual manera haciendo que el tiempo total sea el de 2 seg
# ? t1 = threading.Thread(name="hilo", target= consultar, args= (1, ))
# ? t2 = threading.Thread(name="hilo", target= guardar, args= (1, 'Este es un segundo argumento de prubea' ))
# ? t1.start()
# ? t2.start()
# ? t1.join()
# ? t2.join()

t1 = threading.Thread(name="hilo", target= consultar, args= (1, ))
t2 = threading.Thread(name="hilo_2", target= guardar, args= (1, 'Este es un segundo argumento de prubea' ))

t1.start()
t2.start()

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()


print(f'Tiempo transcurrido:{str(tiempo_fin.second - tiempo_ini.second)}')

# todo Podemos hacer la misma implementacion de los hiloa con el uso de clases