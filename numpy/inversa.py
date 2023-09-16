import numpy as np
import random as ran
ecuacuaciones=np.array([[2,-4,-3],[1,5,-5],[4,2,67]])
resultados=np.array([[15],[5],[20]])
inversa=np.linalg.inv(ecuacuaciones)
print(inversa)
X=inversa@resultados
print(X)
c=ecuacuaciones@X
print(c)
#////////////////////////////////Funcion random

x=[ran.randint(1,100) for _ in range(10)]
print(x)

