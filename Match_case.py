'''Es una sentencia de opciones y tiene el mismo funcionamineto que el switch-case'''
opcion=input('Digite un numero del 1 al 3: ')
match opcion:
    case '1':
        print('Usted puso el digito 1')
    case '2':
        print('Usted puso el digito 2')
    case '3':
        print('Usted puso el digito 3')
    case _:
        print('Usted coloco un digito fuera de rango')