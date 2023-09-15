import os

import Practica_1 as funciones

def menu():
    
    for i in range(17):
        print('*', end='_')
    print('\n\tMi programa.')
    print(' 1. Media Aritmética\n 2. Desviación Estándar\n 3. Burbuja\n 4.Salir');
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
        print('\n\t**MEDIA ARITMETICA**')
        nm=int(input('Digite el numero de muestras->'))
        r1=funciones.media_aritmetica(nm)
        print(f'La media aritmetica es de {r1}')
        
    elif opcion == 2:
        print('\n\t**DESVIACION ESTANDAR**')
        nm=int(input('Digite el numero de muestras->'))
        r2=funciones.desviacion(nm)
        print(f'La desviacion estandar es de {r2}')
        
    elif opcion == 3:
        print('\n\t**BURBUJA**')
        nm=int(input('Digite el numero de muestras->'))
        r3=funciones.burbuja(nm)
        print(f'\nOrdenamiento de las muestras\n',r3)
        
    elif opcion == 4:
        print('\n\t**SALIR**')
        print('Gracias por usar mi pequeño programa creado por python :)\n')
        quit()
        
    else:
        os.system('cls')
        print('OPCION NO ENCONTRADA EN EL MENU')
        
''' MAIN'''
while True:
    Principal()