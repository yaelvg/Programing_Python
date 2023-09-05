'''Algunas funciones para el uso de los strings'''
#Uso de "len" para poder conocer el tamaño de la cadena
c="Alejandro"
print(len(c))
#Impresion por partes
print(c[:] + " Toda la cadena")
print(c[:4] + " Primeras 4 cadenas de cadenas")
print(c[4:9] + " Letras de 'a' a 'o' ")
#Pasar una cadena a mayusculas y minusculas
print(c.upper() + " Cadena en Mayusculas")
print(c.lower() + " Cadena en minisculas")
#Encontrar un elemento en la cadena
print("Encontrando la letra 'e' que este en el espacio ", c.find('e'))
'''Remplazando partes de la cadena'''
x="  Hola Alejandro  "
y=x.replace('Alejandro','Adamaris')
print(y)
#Eliminando espacios en blanco
y=x.lstrip()
print('\n\nTexto con espacion ' + x)
print('Texto sin espacion izquierdos '+ y)
z=x.strip()
print('\n\nTexto sin espacios laterales' + z)
#Uso del starwitch para saber si la cadena empieza con una letra o palabra en especifico
print('\n\n')
q='Alejandro y Valdez'
#Me returna 0 o 1 si la accion es verdadera o falsa
print('La cadena empieza con Valdez ', q.startswith('Valdez'))
print('La cadena empieza con Alejandro ', q.startswith('Alejandro'))