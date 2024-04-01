
# todo Implementation de logs en el testing de aplicaciones entre otros.
import threading
import logging
import time

# ! Podemos crear archivos tipo log para poder llevar un mejor control de cada uno de estos logs en 
logging.basicConfig(level=10,
                    format = '%(asctime)s -%(threadName)s- %(levelname)s - %(message)s',
                    filename= 'Testing.log',
                    filemode= 'a')


def datos(nombre, id):
    try:
        time.sleep(2)
        x = nombre + " usuario nuevo"
        y = int(id)
        logging.debug("Se asignaron los datos correctamente")
    except:
        logging.warning("Datos de tipo incorrectos")
    
    return logging.debug("Datos guardados")

# // principal
if __name__ == "__main__":
    
    logging.info("Inicio del programa")
    
    t1 = threading.Thread(name = 'hilo secundario ', target= datos, args = ('datos de hilo 1', 123))
    
    t1.start()
    t1.join()
    
    logging.info("Proceso terminado")
    
    