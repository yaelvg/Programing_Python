'''Practica numero 2 haciendo uso de clases y metodos - POO.

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 2
Fecha: 26/09/2023
'''
class Persona:
    
    #Constructor
    def __init__(self, nombre : str, edad : int, estura : float, numero : int) -> None:
        self._nombre = nombre
        self._edad = edad
        self._estatura = estura
        self._numero = numero
    #Encapsulamiento
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad: int):
        self._edad = edad
    
    @property
    def estatura(self):
        return self._estatura
    @estatura.setter
    def estatura(self, estaura: float):
        self._estatura = estaura
    
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero: str):
        self._numero = numero
        
    def __str__(self) -> str:
        return f'¡Hola! , Mi nombre es {self._nombre}, tengo {self._edad} años , nací en {2023-self._edad}.\n mido {self._estatura} metros y mi número de contacto es {self._numero} ¡Saludos!'

def llenado():
    for i in range(3):
        
        print(f'\n\tPersona {i+1}:\n')
        nombre_=input('Nombre:')
        edad_=int(input('Edad:'))
        estatura_=float(input('Estatura en metros:'))
        numero_=int(input('Numero:'))
        
        persona=Persona(nombre_,edad_,estatura_,numero_)
        personas.append(persona)

def impresion():
    for i in range(3):
        print(f'\nPersona {i+1}:\n')
        print(personas[i])

'''Funcion principal'''

personas = list()
llenado()
impresion()    
