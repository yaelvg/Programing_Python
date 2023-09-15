import numpy as np

def Principal():
    """Funcion principal que contien las funciones secundarias.
    """
    print('\n\tSistema de ecuacuaciones 3x3\n')
    '''Resultados'''
    x_resultados=np.array([])
    ecuacuaciones=np.array([[2,-4,-4],[1,5,-5],[4,2,67]])
    resultados=np.array([15,5,20])
    '''Siguiendo el modelo
        X=A^(-1)B   
    '''
    inversa=np.linalg.inv(ecuacuaciones)
    print(inversa)
    for i in range(3):
        x=np.dot(inversa[i],resultados[i])
        x_resultados=np.vstack(x)
    print(x_resultados)
    
Principal()