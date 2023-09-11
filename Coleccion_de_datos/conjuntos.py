'''Los conjutos su caracteristica es que ordena los datos y no permite
elementos duplicados
'''
#Este es el primer conjunto
conjunto=set()
conjunto={1,2,3,4}
print(conjunto)
conjunto.add(6)
print(conjunto)
conjunto2={5,7,8,9}
conjunto |= conjunto2
print(conjunto)
print(type(conjunto))
