import numpy as np

# Crear una lista para almacenar los arrays ingresados por el usuario
arrays = []

# Solicitar al usuario que ingrese los arrays uno por uno
while True:
    entrada = input("Ingresa un array (separa los valores con espacios, 'q' para terminar): ")
    
    if entrada.lower() == 'q':
        break
    
    try:
        # Convertir la entrada en un array NumPy y agregarlo a la lista
        array = np.array([float(x) for x in entrada.split()])
        arrays.append(array)
    except ValueError:
        print("Entrada no válida. Introduce valores separados por espacios.")
print(arrays)
# Combinar los arrays en un solo array utilizando numpy.vstack
if len(arrays) > 0:
    matriz_resultante = np.vstack(arrays)
    print("Matriz resultante:")
    print(matriz_resultante)
else:
    print("No se ingresaron arrays.")