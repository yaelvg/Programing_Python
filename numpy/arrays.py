import numpy as np
array1=np.array([1,2,3,4])
print(type(array1))
#Nueva matriz 2x2
#matriz_1=np.matrix([[1,2],[1,2]])
#print(matriz_1)
#Podemos crear un array de numpy con otros arrya dentro del mismo.
array2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('Esto es un array de numpy\n', array2)
#uso del shape'Forma'
print(np.shape(array2))
#reshape
newarray=array2.reshape(4,3)
print(newarray)