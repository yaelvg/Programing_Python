'''Practica numero 3 haciendo uso de Herencia y Polimorfismo

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 3
Fecha: 4/10/2023
'''
from abc import ABCMeta, abstractmethod

#Clase madre
class Mascota(metaclass=ABCMeta): 
    """Clase Madre
    """
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__duenio = duenio
        self.__tipo = tipo
    
    #getters y setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre =nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad =edad
    
    @property
    def duenio(self):
        return self.__duenio
    @duenio.setter
    def duenio(self, duenio):
        self.__duenio =duenio
    
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo =tipo
    
    #Metodo habla
    @abstractmethod
    def habla(self):
        pass
    
    #Metodo tostring
    @abstractmethod
    def __str__(self) -> str:
        pass

class Domestica(Mascota, metaclass= ABCMeta):
    """Clase Domestica heradada

    Args:
        Mascota (class): Clase madre
    """
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, ternura: int):
        Mascota.__init__(nombre, edad, duenio, tipo)
        self.__ternura = ternura
        
    #getters y setters
    @property
    def ternura(self):
        return self.ternura
    @ternura.setter
    def ternura(self,ternura):
        self.ternura =ternura
    
    #toString
    @abstractmethod
    def __str__(self) -> str:
        pass

class Exotica (Mascota, metaclass=ABCMeta) :
    """Clase Exotica heredada

    Args:
        Mascota (class): Clase madre
    """
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int):
        Mascota.__init__(nombre, edad, duenio, tipo)
        self.__peligro = peligro
    
    #getters y setters
    @property
    def peligro(self):
        return self.__peligro
    @peligro.setter
    def peligro(self,peligro):
        self.__peligro = peligro
    
    #toString
    @abstractmethod
    def __str__(self) -> str:
        pass

#clase submadre Domestica
class Gato(Domestica):
    
    def __init__(self, nombre : str, edad: int, duenio: str) -> None:
        Mascota.__init__(nombre, edad, duenio)
    
    def habla()-> str:
        pass
    
    def __str__(self) -> str:
        pass

class Perro(Domestica):
    
    def __init__(self, nombre: str, edad: int, duenio: str,):
        Mascota.__init__(nombre, edad, duenio)
    
    def habla()-> str:
        pass
    
    def __str__(self) -> str:
        pass
    
#clase submadre Exotica
class Vivora(Exotica):
    
    def __init__(self, nombre : str, edad: int, duenio: str):
        Mascota.__init__(nombre, edad, duenio)

    def habla()-> str:
        pass
    
    def __str__(self) -> str:
        pass
    
class Tigre(Exotica):
    
    def __init__(self, nombre : str, edad: int, duenio: str)-> None:
        Mascota.__init__(nombre, edad, duenio)

    def habla()-> None:
        pass
    
    def __str__(self) -> str:
        pass
    
class Dinosaurio(Exotica, metaclass=ABCMeta):
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo_dinosaurio: str)-> None:
        Mascota.__init__(nombre, edad, duenio)
        self.__tipo_dinosaurio = tipo_dinosaurio
    
    @property
    def tipo_dinosaurio(self):
        return self.__tipo_dinosaurio
    @tipo_dinosaurio.setter
    def tipo_dinosaurio(self,tipo_dinosaurio):
        self.__tipo_dinosaurio = tipo_dinosaurio
        
    @abstractmethod
    def __str__(self) -> str:
        pass
#Subclasese de dinosaurio

class Brontosaurio(Dinosaurio):
    
    def __init__(self, nombre : str, edad: int, duenio: str):
        Mascota.__init__(nombre, edad, duenio)

    def habla(self)-> str:
        pass
    
    def __str__(self) -> str:
        pass

class Raptor(Dinosaurio):
    
    def __init__(self, nombre : str, edad: int, duenio: str):
        Mascota.__init__(nombre, edad, duenio)
    
    def habla(self)-> str:
        pass
    
    def __str__(self) -> str:
        pass
    
class Trex(Dinosaurio):
    
    def __init__(self, nombre: str, edad: int, duenio: str) -> None:
        Mascota.__init__(nombre, edad, duenio)
    
    def habla(self)-> str:
        pass
    
    def __str__(self) -> str:
        pass
    
    