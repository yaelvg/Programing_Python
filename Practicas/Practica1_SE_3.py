'''
Nombre: Yael ALejandro Valdez Gonzalez
Boleta: 2022640608
Practica: 1
Fecha: 16/09/2023
'''

import numpy as np

def error(filas : list): 
    """Error generada por falta de argumentos ingresados por el usuario

    Args:
        filas (list): ingresa la lista de listas creada por el usuario en la función
        ingreso_datos():

    Returns:
        funcion: retorna a la funcion ingreso_datos():
    """ 
    #Variables auxiliares
    n = 3
    posicion = 0
    
    while n > 0:
        #Analiza fila por fila la lista de entrada
        if len(filas[posicion]) != 3:
            print('Error al ingresar los datos')
            return ingreso_datos()
        n -= 1
        posicion += 1
       
def ingreso_datos():
    """Ingreso de datos

    Returns:
        array: retorna un array de arrays que simulan la matriz echa por el usuario
    """
    
    print('\n\nIngrese sus datos por filas (Separe con espacios los datos):')
    #Variables auxilares
    filas = []
    n = 3
    i = 1
    while n > 0 :
        datos = input(f'fila[{i}]->')
        try:
            '''Separa los datos con la funcion split para despues
            almacenarlos en un array y convertilos a flotante,
            si se ingresa un dato str vuelve al principio de la funcion
            '''
            fila = np.array([float(i) for i in datos.split()])
            filas.append(fila)
            n -= 1
            i += 1
        except:
            print('Entrada invalida')
    error(filas)
    '''Con la funcion vstack se concatenan las listas ingresadas por el usuario y la retorna'''   
    filas = np.vstack(filas)
    return filas

def ingreso_resultados():
    """Ingreso de resultados
    
    Returns:
        array: Retorna un array(vector) que contiene los resultados de las ecuaciones
    """
    print('\n\nIngreso de resultados')
    #variables auxiliares
    vector = []
    n = 3
    i = 1
    while n > 0:
        try:
            '''Si el dato ingresado por el usuario es del tipo str vuelve al inicio del bucle'''
            dato = int(input(f'fila[{i}]->'))
            vector.append(dato)
            n -= 1
            i += 1
        except:
            print('Entrada invalida')
    '''convierte la lista a un array para despues retornarlo'''
    vector = np.vstack(vector)
    return vector
    
def ejemplo():
    """Ejemplo de solucion de un sistema de ecuaciones propuesto
    """
    print('\nSe presenta un ejemplo de como soluciona el programa un sistema de ecuaciones\n')

    print('\nEjemplo de un sistema de ecuaciones')
    print('\t2x - 4y - 3z = 15\n\tx + 5y - 5z = 5\n\t4x + 2y + 67z = 20')
    
    ecuacuaciones = np.array([[2,-4,-3],[1,5,-5],[4,2,67]]) 
    resultados = np.array([[15],[5],[20]])
    
    print('Se guardan las ecuaciones en una matriz\n', ecuacuaciones,
          '\n\n Y en un vector los resultados\n', resultados)
    print('\nDel modelo: X=A^(-1)B')
    
    inversa = np.linalg.inv(ecuacuaciones)
    #print('Obtenemos la inversa\n', inversa)
    
    print('\nSe hace el producto entre matrices respecto al modelo mostrado anteriormente')
    x = inversa@resultados
    
    print('Soluciones:\n')
    for indice, valor in enumerate(x):
        print(f'x[{indice}] = {valor}')
    
    print('\nPara confirmar hacemos el producto entre el vector de resultadosy la matriz de ecuaciones')
    resultados = ecuacuaciones@x
    print('Como resultado obtenemos el vector de los resultados del sistema\n', resultados)
    
def principal():
    
    """Funcion principal que contien las funciones secundarias.
    """
    print('\n\tSistema de ecuacuaciones 3x3\n')
    
    for i in range(20): print('*', end='_')
    ejemplo()
    for i in range(20): print('*', end='_')
    
    '''Solucion propuesta por el usuario'''
    ecuaciones = ingreso_datos()
    resultados = ingreso_resultados()
    
    '''Inversa de matriz ecuaciones'''
    inversa = np.linalg.inv(ecuaciones)
    
    '''Vector resultados'''
    x = inversa@resultados
    print('\n\nSoluciones:\n')
    for indice, valor in enumerate(x):
        print(f'x[{indice+1}] = {valor}')
    print('\nComprobacion')
    y = ecuaciones@x
    print(y)    
'''MAIN'''
principal()
