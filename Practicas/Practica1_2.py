'''
Nombre: Yael ALejandro Valdez Gonzalez
Boleta: 2022640608
Practica: 1
Fecha: 16/09/2023
'''

'''Este archivo contiene funciones que se utilizaran en el programa principal'''
import random as r
import numpy as np

from numpy import mean

def ingreso_muestras(nmuestras: int):
    """"Funcion para almacenas las muestras ingresadas

    Args:
        nmuestras (int): Numero total de las muestras

    Returns:
        lista: Lista con los datos ingresados por el usuario
    """
    muestras = list()
    
    print('Digite las muestras')
    for i in range(nmuestras):
        inp = int(input('*->'))
        muestras.append(inp)
        
    return muestras

def media_aritmetica(nmuestras: int):
    """Retorna la media artimetica de los datos proporcionados


    Args:
        nmuestras (int): Numero de muestras 
    """
    '''Lista vacia para agrupar muestras'''
    x = ingreso_muestras(nmuestras)
    return mean(x)

def desviacion(nmuestras: int):
    """Desviacion Estandar
        Realiza la desviacion estandar de determinados datos
    Args:
        nmuestras (int): Numero de muestras
    """
    x = ingreso_muestras(nmuestras)
    return np.std(x)

def burbuja(nmuestras: int):
    """Ordenamiento burbuja
        Realiza un ordenamiento burbuja
    Args:
        nm (int): Numero de muestras
    """
    
    l_superior = int(input('Especifica el número más alto para los números aleatorios:'))
    #Genera una lista con numeros aleatorios
    numeros = [r.randint(0,l_superior) for _ in range(nmuestras)] 
    print('Los datos generados son los siguientes', numeros)
    
    '''Ordenamiento'''
    '''El rango se va haciendo mas pequeño conforme el numero de
    datos organizados aumente para .
    '''
    for i in range(nmuestras-1):
        for j in range(nmuestras-1-i):
            '''Realiza un intercambio dependiendo de la posicion de datos'''
            if numeros[j] < numeros[j+1]:
                numeros[j] , numeros[j+1] = numeros[j+1] , numeros[j]
                
    return numeros