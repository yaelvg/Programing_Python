import Practica3_2 as P3

mascotas=[]

#Menu
def menu() -> None:
    print('\t****Adopta una mascota****')
    print('\t\t"El UPIITO"')
    print('Elija la categoria de su futuro acompañente.')
    print('1. Mascotas Domésticas')
    print('2. Mascotas Exóticas')
    print('3. Salir')
    opcion = input('-> ')
    if opcion == "1":
        pass
            #mascota_domestica()
    elif opcion == "2":
        pass
           # mascota_exotica()
    else:
        print("Opción no valida, seleccione una del menu.")
        menu()