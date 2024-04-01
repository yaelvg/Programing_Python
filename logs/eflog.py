
# * Podemos implementar los logs de una manera eficiente
import logging

# * --------------Creacion del logger--------------
logger = logging.getLogger('app') # NOMBRE
logger.setLevel(logging.DEBUG) #! Tomamos el nivel mas bajo
# Creacion del handler
handler = logging.FileHandler('app.log')
# Se crea un formato y se lo asigna al handler
format = logging.Formatter('%(asctime)s| %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(format)
# se agrega al logger un handler
logger.addHandler(handler)
# * ---------------------------------------------------

# ? Si queremos ver los loggers en pantalla, creamos un StreamHandler
handler2 = logging.StreamHandler()
handler2.setFormatter(format)
logger.addHandler(handler2)


def ejemplo():
    
    logger.info('Este es un mensaje informativo')
    return 

if __name__ == '__main__':
    ejemplo()