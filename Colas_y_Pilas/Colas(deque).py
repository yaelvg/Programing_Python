from collections import deque
'''Para las colas tenemos sus siglas en ingles que son FIFO (First In First Out)
Para el uso de las colas vamos a importar la libreria deque
'''
cola=deque()
#Añadir elementos a la cola
cola=deque(['Yael','Ada','Azul'])
#Podemos agregar datos a la cola con la funcion append
cola.append('Marco')
cola.append('Norma')
print('\n Cola actualizada')
print(cola)
print('\n Nueva cola')
#Para las colas tenemos la funcion popleft que me saca los elemtos de izquiera a derecha
lista=list()
for i in range(len(cola)):
    lista.append(cola.popleft())
print('Se ha vaciado la cola en la lista')
print(lista)