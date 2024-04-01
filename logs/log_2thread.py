import threading
import logging
import time

# todo De igual manera podemos conocer el hilo en donde se esta ejecutando un logging

logging.basicConfig(level=10,
                    format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s')

def consultar(name):
    time.sleep(2)
    logging.debug('Datos obtenidos' + str(name))
    return

def guardar(name, data):
    logging.debug('datos guardados ' + str(name) + ' y data ' + str(data))
    time.sleep(5)
    return

if __name__ == '__main__':
    
    logging.info('Se ha iniciado el principal')
        
    # * Implementacion de hilos

    t1 = threading.Thread(name= 'hilo1', target=consultar, args= ('hilo1',))
    t2 = threading.Thread(name= 'hilo2', target= guardar, args= ('hilo2', 'este es el segundo hilo')) 

    t1.start()
    t2.start()

    logging.debug('Inicio de hilo')

    t1.join()
    t2.join()

    logging.debug('Union lista')
