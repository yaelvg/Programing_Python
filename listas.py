'''
#Esto es una lista en python
lista=[1,2,3,'Hola mundo',[8,4,3]]
#Impresion de las listas en python
print(lista[:])
print('Lista con indices negativos "Reverso"')
print(lista[::-1])
print('Lista con indices negativos -2')
print(lista[-2:])
print('\nOrden ascendente\n')
#Otra forma de ordenar la lista en orden ascendete
lista_1=[3,4,3,1,7,8,5]
lista_1.sort()
print(lista_1)
#Uso del in para saber si hay un elemento en una lista
x=5 in lista_1
print(x)
'''
'''Podemos modificar la lista por tramos'''
listaNueva=list() #Forma de crear una lista vacia
listaNueva=['a', 'b', 'c', 'd', 'e', 'f']
print(listaNueva)
listaNueva[:3]=['A', 'B', 'C']
print('\nSe ha modificado la lista\n')
print(listaNueva)
#Tamaño de una lista
y=len(listaNueva)
print(y)
print('\n\n')
'''Uso de listas anidadas dandoles un uso de arreglos dimensionales'''
m1=[[5,3,1],[12,0,2]]
print(m1[-1][-2])