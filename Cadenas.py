# Variables del ejercicio (no las modifiques)
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Completa el ejercicio
cadena_volteada=cadena_corrupta[::-1]
print(cadena_volteada)
#Extrae el nombre
nombre=cadena_volteada[:12]
print(nombre)
#nota
nota=cadena_volteada[13:16]
print(nota)
#Materia
materia=cadena_volteada[17:]
print(materia)
#ultima cadena
cadena_formateada= nombre + ' ha sacado un ' + nota + ' en ' + materia
print(cadena_formateada)