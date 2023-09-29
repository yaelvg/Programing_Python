def potencia(base, expo, modulo):
    if modulo == 1:
        return 0
    #assert (modulo - 1) * (modulo - 1)
    r = 1
    base %= modulo
    while expo > 0 :
        if expo % 2 == 1:
            r = (r * base) % modulo
        expo = expo >> 1
        base = (base * base) % modulo
    return r
x=int(input('base:'))
y=int(input('expoe:'))
z=int(input('Modulo:'))
print(potencia(x,y,z))