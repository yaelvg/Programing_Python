'''Variables temporales en el uso del for para la eficiencia del programa '''
lista=['Azul','Ada','Norma','Marco','Ale']
'''Lista de nombre'''
for indice, nombre in enumerate(lista):
    print(indice, nombre)
'''Esto provoca que no haya varibales vasura por lo que es mas eficiente como se menciono
Lo que regresa la función enumerate es una tupla lo que me permite lo anterior

'Lista con subtuplas que contiene la posicion y el valor'

'''
print('\n\n')
'''Otra funcion parecida al enumarete es el items() que hace una funcion parecida
pero solo funciona en diccionarios'''
dic={1:'ale',2:'Ada',3:'azul'}
for llave, letra in dic.items():
    print(llave, letra)
