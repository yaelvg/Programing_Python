'''lista=[67,2,56,21,67,100,40,16]
x=len(lista)
for i in range(x):
    for j in range(x):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1]=lista[j+1],lista[j]
print(lista)
'''
def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n):       # <-- bucle padre
        for j in range(n-1): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos)
#Este es un pequeño cambio