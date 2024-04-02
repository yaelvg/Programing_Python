from getpass import getpass
# * Haciendo uso del getpass

class Ingreso():
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def bienvenida(self) -> None:
        print(f'Bienvenido {self.__username}')

if __name__ == '__main__':
    usr=input('ingresa tu usuario:')
    password=getpass('password:')
    us= Ingreso(usr, password)
    us.bienvenida()