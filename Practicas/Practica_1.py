'''Este archivo contiene funciones que se utilizaran en el programa principal'''
import numpy as np
from numpy import mean
import random
def aleatorio(n: int, lm: int):
    """Aleatorio
        Genera numeros aleatorios para despues
        almacenarlos en una lista
    Args:
        n (int): Cantidad de numeros generados
        lm (int): Limite superior de numeros aleatorios
    """
    lista=list()
    while n!=0:
        numero=random.randint(1,lm)
        lista.append(numero)
        n-=1
    return lista
def media_aritmetica(nm: int):
    """Retorna la media artimetica de los datos proporcionados


    Args:
        nm (int): Numero de muestras 
    """
    '''Lista vacia para agrupar muestras'''
    muestras=list()
    print('Digite las muestras')
    for i in range(nm):
        inp=int(input('*->'))
        muestras.append(inp)
    return mean(muestras)
def desviacion(nm: int):
    """Desviacion Estandar
        Realiza la desviacion estandar de determinados datos
    Args:
        nm (int): Numero de muestras
    """
    muestras=list()
    print('Digite las muestras')
    for i in range(nm):
        inp=int(input('*->'))
        muestras.append(inp)
    return np.std(muestras)
def burbuja(nm: int):
    """Ordenamiento burbuja
        Realiza un ordenamiento burbuja
    Args:
        nm (int): Numero de muestras
    """
    lm=int(input('Especifica el número más alto para los números aleatorios:'))
    lst=aleatorio(nm,lm)
    print('Los datos generados son los siguientes', lst)
    '''Ordenamiento'''
    for i in range(nm-1):
        for j in range(nm-1-i):
            '''El rango se va haciendo mas pequeño conforme el numero de
                datos organizados aumente.
            '''
            if lst[j] < lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst