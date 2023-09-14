import Practica_1 as funciones
import os
def menu():
    '''This function is used to show the menu'''
    try:
        opcion=int(input("Opcion-> "))
        """Almacena la opcion seleccionada del usuario"""
    except:
        os.system('cls')
        print('Opcion invalida')
        return menu()
        """Se realiza una limpieza de pantalla en caso de ingresar datos tipo str"""
    if opcion == 1:
        print('\n\t**Opcion 1**')
        nm=int(input('Digite el numero de muestras->'))
        r1=funciones.media_aritmetica(nm)
        print(f'La media aritmetica es de {r1}')
    elif opcion == 2:
        print('\n\t**Opcion 2**')
    elif opcion == 3:
        print('\n\t**Opcion 3**')
    elif opcion == 4:
        print('\n\t**Opcion 4**')
        print('Gracias por usar mi pequeño programa creado por python :)\n Salu2 profe')
        quit()
    else:
        os.system('cls')
        print('Opcion no encontrada en el menu')
''' MAIN'''
while True:
    print('\nMi programa.')
    print('1. Media Aritmética\n2. Desviación Estándar\n3. Burbuja\n4.Salir\n');
    '''Menu del programa'''
    menu()