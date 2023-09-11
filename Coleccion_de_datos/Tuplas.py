'''Tuplas son interables '()' '''
tupla=(100,'hola',[2,3,4],3.14)
#impresion de la tupla con enumerate
for indice, valor in enumerate(tupla):
    print(indice, valor)

print('Error por tublas, "Valores iterables"')
#tupla[0]=120