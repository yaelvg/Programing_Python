def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    assert (modulus - 1) * (modulus - 1)
    result = 1
    base = base % modulus
    while exponent > 0 :
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
x=int(input('base:'))
y=int(input('Exponente:'))
z=int(input('Modulo:'))
print(modular_pow(x,y,z))