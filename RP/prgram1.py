'''
Clases con uso de constructores, encapsilamiento- getters y setter
'''
class alumno():
    """Clase con atributos
    """
    #* Inicializacion de atributos 
    def __init__(self, nombre : str, boleta : int):
        self.__nombre = nombre
        self.__boleta = boleta
        
    def __str__(self):
        return f'Hola mi nombre es {self.__nombre}, y numero {self.__boleta}'
    
    @property
    #*getter
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#! Principal
alumnono1= alumno('yael',1203)
#* Aqui le asignamos un nuevo valor para este objeto
alumnono1.nombre = 'ale'
print(alumnono1)
        