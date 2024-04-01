
# todo Implementation de logs en el testing de aplicaciones entre otros.

import logging

# * Contamos con ciertas etiquetas para cada caso de infromacion
# * DEBUG = 10
# * INFO = 20
# * WARNING = 30
# * ERROR = 40
# * CRITICAL = 50

# ? Mandamos a llamar los mensajes a base de la siguiente linea
#? El numero indica el nivel del tipo de mensaje
# logging.basicConfig(level=10)
#Podemos agregar un formato 
logging.basicConfig(level=10,
                    format = '%(asctime)s, %(levelname)s- %(message)s')


def datos(nombre, id):
    try:
        x = nombre + "usuario nuevo"
        y = int(id)
        logging.debug("Se asignaron los datos correctamente")
    except:
        logging.warning("Datos de tipo incorrectos")
    
    return logging.debug("Datos guardados")

# // principal
if __name__ == "__main__":
    
    datos('Ale', 1234)
    logging.info("Fin del proceso")