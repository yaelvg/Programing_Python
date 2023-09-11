'''Es una coleccion de datos que cada elemento cuenta con una llave unica
diccionario={}
diccionario={key:value}
'''
def busqueda(palabra: str):
    '''Busqueda de colores

    Uso del try    
    '''
    try:
        palabra in dic_1
        print(dic_1[palabra])
    except:
        print('No se encontro la palabra')


dic_1={}
print(type(dic_1))
dic_1={'azul':'blue','rojo':'red','negro':'black'}
'''Contiene una llave 'español' al 'ingles' '''
#Vamos a implementar una funcion para el uso de los diccionarios con try an except
palabra=input('Escriba el color:')
busqueda(palabra)
#Bloque 2
print('\n\n')
dic_2={0:'azul',1:'rojo',2:'negro'}
#acceder a elementos del diccionario 
x=dic_2[0]
print(f'Llave 0 valor de {x}')
#Sumando elementos de diccionarios
nombre={'Yael':20,'Ada':17,'Norma':38,'Marco':56}
nombre['Yael']+=1
print(f'Incrementando la edad de yael en ', nombre['Yael'])
#accediendo al diccionario con enumerate
for name, edad in enumerate(nombre):
    print(name, edad)
'''Y como se vio anteriormente tambien podemos tener un lista de tuplas'''
lista=list()
lista.append(dic_1)
lista.append(dic_2)
lista.append(nombre)
print(lista)