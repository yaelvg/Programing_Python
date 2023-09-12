'''Para las listas tenemos un sintaxis con []'''
lista=list()
lista=['Ale','azul','Ada']
print(lista)
#Podemos tener lista de listas lo que me ayuda poder tener un mejor manejo de datos
lista_edades=[20,11,17]
lista_profesiones=['Universidad','Primaria','Idiomas']
lista_final=list()
lista_final.append(lista)
lista_final.append(lista_edades)
lista_final.append(lista_profesiones)
print(lista_final)
'''De igual manera podemos tener listas llenas de tuplas'''
print('\n\nLista de tuplas...')
tuplan=('Yael','Ada','Azul')
tuplae=(20,17,11)
lista2=list()
lista2.append(tuplan)
lista2.append(tuplae)
print(lista2)
'''Lista de diccionarios'''
print('\nLista de diccionarios')
dicne={'Yael':20,'Ada':17,'Azul':11}
dicne['Marco']=55
'''Forma de agregar un elemento en el diccionario [Key]=Value'''
print(dicne)
lista_dic=list()
dic2={1:'red',2:'green',3:'yellow'}
lista_dic.append(dicne)
lista_dic.append(dic2)
print(lista_dic)
