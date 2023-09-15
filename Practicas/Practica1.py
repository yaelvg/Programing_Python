import Practica_1 as funciones
import os
def menu():
    '''This function is used to show the menu'''
    for i in range(17):
        print('*', end='_')
    print('\n\tMi programa.')
    print(' 1. Media Aritmética\n 2. Desviación Estándar\n 3. Burbuja\n 4.Salir');
    for i in range(17):
        print('*', end='_')
    '''Menu del programa'''
    try:
        opcion=int(input("\nOpcion-> "))
        """Almacena la opcion seleccionada del usuario"""
    except:
        os.system('cls')
        print('OPCION INVALIDA')
        return menu()
        """Se realiza una limpieza de pantalla en caso de ingresar datos tipo str"""
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
    menu()