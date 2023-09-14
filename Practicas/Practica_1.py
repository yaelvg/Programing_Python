'''Este archivo contiene funciones que se utilizaran en el programa principal'''
import numpy as np
from numpy import mean
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