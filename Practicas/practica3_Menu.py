import Practica3_2 as P3
import random as rand
mascotas=[]

def mostrar_mascotas():
    for numero, mascota in enumerate(mascotas):
        print(f'\nMascota [{numero+1}]')
        print(mascota)
        
def mascota_domestica(duenio: str):
    n=0
    while True:
        if n == 0:
            tipo=int(input('¿Que animal te gustaria adquirir?\n***1. Perro\n***2. Gato\n->'))
            if tipo == 1 or tipo == 2:
                print('Buena y muy adorable eleccion!!!')
                n+=1
            else:
                print('Opcion no valida, intentelo de nuevo') 
        if n != 0 :
            ternura=int(input('Nivel de ternura rango(1-10) ->'))
            
            if ternura > 10:
                print('Fuera de rango. El rango es de 1 a 10')
            elif ternura > 0 and ternura <= 10:
                break
    ternura =str(ternura)
    print(type(ternura))
    nombre=input('Nombre de tu futuro y tierno acompañante: ')
    print('Su acompañante esta listo c:')
    edad=rand.randint(0,10)
    edad=str(edad)
    print(type(edad))
    if tipo == 1:
        tipo=str('Perro')
        domestico=P3.Perro(nombre,edad,duenio,tipo,ternura)
        print('\n\n')
        domestico.habla()
    else:
        tipo='Gato'
        domestico=P3.Gato(nombre,edad,duenio,tipo,ternura)
        print('\n\n')
        domestico.habla()
        
    mascotas.append(domestico)
        
def mascota_exotica(duenio):
    n=0
    while True:
        if n == 0:
            tipo=int(input('¿Que animal te gustaria adquirir?\n***1. Vivora\n***2. Tigre\n***3. Dinosaurio\n->'))
            if tipo == 1 or tipo == 2 or tipo == 3:
                print('Buena y muy peligrosa eleccion!!!')
                n+=1
            else: print('Opcion no valida, intentelo de nuevo') 
        if n != 0 :
            peligro=int(input('Nivel de peligro rango(1-10) ->'))
            
            if peligro > 10:
                print('Fuera de rango. El rango es de 1 a 10')
            elif peligro > 0 and peligro <= 10:
                n=0
                break
    nombre=input('Nombre de tu futuro y peligroso acompañante: ')
    edad=rand.randint(0,10)
    if tipo == 1:
        exotico=P3.Vivora(nombre,edad,duenio,tipo,peligro)
        exotico.habla()
    elif tipo == 2:
        exotico=P3.Tigre(nombre,edad,duenio,tipo,peligro)
        exotico.habla()
    else:
        while True:
            if n == 0:
                tipo=int(input('¿Que especie de dinosaurio te gustaria adquirir?\n***1. Brontosaurio\n***2. Raptor\n***3. Trex\n->'))
                if tipo == 1:
                    print('Una opcion aun mas terrorifica ')
                    exotico=P3.Brontosaurio(nombre,edad,duenio,tipo,peligro)
                    exotico.habla()
                    break
                if tipo == 2:
                    print('Una opcion aun mas terrorifica ')
                    exotico=P3.Raptor(nombre,edad,duenio,tipo,peligro)
                    exotico.habla()
                    break
                if tipo == 3:
                    print('Una opcion aun mas terrorifica ')
                    exotico=P3.Trex(nombre,edad,duenio,tipo,peligro)
                    exotico.habla()
                    break
                else: print('Opcion no valida, intentelo de nuevo') 
                          
    print('Tu peligroso amigo esta listo')
    mascotas.append(exotico)

def menu() -> None:
    n=0
    while True:
        
        print('\t****Adopta una mascota****')
        print('\t\t"El UPIITO"')
        if n == 0:
            duenio=input("Ingresa tu nombre: ")
        print('Elija la categoria de su futuro acompañente.')
        print('1. Mascotas Domésticas')
        print('2. Mascotas Exóticas')
        print('3. Salir')
        opcion = input('-> ')
        
        if opcion == "1":
          
            mascota_domestica(duenio)
        elif opcion == "2":
            
            mascota_exotica(duenio)
        elif opcion == "3":
            print('Disfruta la compañia de tu(s) mascota(s)')
            break
        else:
            print("Opción no valida, seleccione una del menu.")
        n+=1
    mostrar_mascotas()
menu()