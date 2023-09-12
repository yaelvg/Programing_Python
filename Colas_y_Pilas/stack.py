'''En la programacion en python no esta como tal una funcion para implementar las
pilas pero podemos utilizar una lista con funciones de manejo de lista como la cual
es pop()
Sus siglas en ingles LIFO (Last in firt out)
'''
pila=[1,2,3,4,5,6,7,8,9,10]
print('This is stack', pila)
#Vamos a extraer el ultimo dato de mi pila con el uso de la funcion POP
#Vamos a basear la 'pila' y pondremos los datos en un 'lista'
lista=list()
for i in range(len(pila)):
    lista.append(pila.pop())
print(lista)