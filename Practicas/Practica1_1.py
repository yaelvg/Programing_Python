'''
Nombre: Yael ALejandro Valdez Gonzalez
Boleta: 2022640608
Practica: 1
Fecha: 16/09/2023
'''

import os

import Practica1_2 as funciones

def menu():
    """Muestra el menu en la funcion principal
    """
    
    for i in range(17): print('*', end='_')
    print('\n\tMi programa.')
    print(' 1. Media Aritmética\n 2. Desviación Estándar\n 3. Burbuja\n 4.Salir')
    for i in range(17): print('*', end='_')
        
        
def Principal():
    '''Muestra el menu y ejecuta las funciones secundarias'''
    '''Menu del programa'''    
    menu()
    
    try:
        opcion = int(input("\nOpcion-> "))
        """Almacena la opcion seleccionada del usuario"""
        
    except:
        '''No permite el ingreso de datos tipos str
        Returns: retorna la funcion principal y hace una limpieza de pantalla
        type: Funcion '''
        os.system('cls')
        print('OPCION INVALIDA')
        
        return Principal()
       
    if opcion == 1:
        print('\n\n\t**MEDIA ARITMETICA**')
        
        n_muestras = int(input('Digite el numero de muestras->'))
        '''Retorna la media aritmetica a la variable respuesta'''
        respuesta = funciones.media_aritmetica(n_muestras)
        print(f'La media aritmetica es de {respuesta}\n')
        
    elif opcion == 2:
        print('\n\n\t**DESVIACION ESTANDAR**')
        
        n_muestras = int(input('Digite el numero de muestras->'))
        '''Retorna la desvieacion estandar a la variable respuesta'''
        respuesta = funciones.desviacion(n_muestras)
        print(f'La desviacion estandar es de {respuesta} \n')
        
    elif opcion == 3:
        print('\n\n\t**BURBUJA**')
        4
        n_muestras = int(input('Digite el numero de muestras->'))
        '''Retorna una lista ordenada a la variable respuesta'''
        respuesta = funciones.burbuja(n_muestras)
        print(f'\nOrdenamiento de las muestras\n',respuesta,'\n')
        
    elif opcion == 4:
        print('\n\n\t**SALIR**')
        
        print('Gracias por usar mi pequeño programa creado por python :)\n')
        quit()
        
    else:
        os.system('cls')
        print('OPCION NO ENCONTRADA EN EL MENU')
        
''' MAIN'''
while True:
    Principal()