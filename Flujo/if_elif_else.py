'''Repaso de como funciona la estrucutura de if'''
a=int(input('Valor a:'))
b=int(input('Valor de b: '))
if a==10 and b==20:
    print('El valor de de b es el doble de a')
elif a>b:
    print('El valor de a es mayor al de b')
elif a<b:
    print('El valor de b es mayor al de a')
else:
    print('El valor de a es igual al de b')