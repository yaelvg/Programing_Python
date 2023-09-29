'''Practica numero 2 haciendo uso de clases y metodos - POO.

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 2
Fecha: 26/09/2023
'''
class Persona:
    
    def __init__(self, nombre : str, edad : int, estura : float, numero : int) -> None:
        #Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estura
        self.__numero = numero
        
    #Encapsulamiento setters y getters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad
    
    @property
    def estatura(self):
        return self.__estatura
    @estatura.setter
    def estatura(self, estaura: float):
        self.__estatura = estaura
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero
        
    def __str__(self) -> str:
        return f'¡Hola! , Mi nombre es {self.__nombre}, tengo {self.__edad} años, nací en {2023-self.__edad}.\n mido {self.__estatura} metros y mi número de contacto es {self.__numero} ¡Saludos!'

def llenado():
    """Guarda informacion proporcionada por el usuario
    """
    for i in range(3):
        
        print(f'\n\tPersona {i+1}:\n')
        nombre_=input('Nombre:')
        edad_=int(input('Edad:'))
        estatura_=float(input('Estatura en metros:'))
        numero_=int(input('Numero:'))
        
        #Se crea una instacia de tipo persona para agregarla a una lista
        persona=Persona(nombre_,edad_,estatura_,numero_)
        personas.append(persona)

def impresion():
    """Impresion de datos
    """
    #Recorre las instancias de la lista de tipo Persona
    for i in range(3):
        print(f'\nPersona {i+1}:\n')
        print(personas[i])

'''Funcion principal'''

#Lista que contien instacias de tipo Persona
personas = list()
llenado()
impresion()    
