'''Funcionamiento del while y como es su estructura'''
CONSTANTE=0
x=1
while CONSTANTE<10:
    print('Valor de la constante incrementada: ', CONSTANTE)
    CONSTANTE+=1
print('\n\n')
c=1
print('Tabla de multiplicar')
while c<=10:
    print(c,'x','2','=',c*2)
    c+=1
'''usos del break y continue'''
#Break rompe el ciclo y continue rope solo la iteracion
x=10
for i in range(x):
    if i==5:
        print('Aqui va el 5')
        continue
    print(i)
for i in range(x):
    if i==5:
        print('Aqui se rompe el bucle')
        break
    print(i)