import os

import Practica_1 as funciones

def menu():
    
    for i in range(17):
        print('*', end='_')
        
    print('\n\tMi programa.')
    print(' 1. Media Aritmética\n 2. Desviación Estándar\n 3. Burbuja\n 4.Salir')
    
    for i in range(17):
        print('*', end='_')
        
        
def Principal():
    '''Muestra el menu y ejecuta las funciones secundarias'''
    '''Menu del programa'''    
    menu()
    
    try:
        opcion=int(input("\nOpcion-> "))
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
        
        n_muestras=int(input('Digite el numero de muestras->'))
        respuesta=funciones.media_aritmetica(n_muestras)
        print(f'La media aritmetica es de {respuesta}\n')
        
    elif opcion == 2:
        print('\n\n\t**DESVIACION ESTANDAR**')
        
        n_muestras=int(input('Digite el numero de muestras->'))
        respuesta=funciones.desviacion(n_muestras)
        print(f'La desviacion estandar es de {respuesta} \n')
        
    elif opcion == 3:
        print('\n\n\t**BURBUJA**')
        4
        n_muestras=int(input('Digite el numero de muestras->'))
        respuesta=funciones.burbuja(n_muestras)
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