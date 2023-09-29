from abc import ABCMeta, abstractmethod

class Figura(metaclass=ABCMeta):
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def __str__ (self) -> None:
        pass
class Cuadrado(Figura):
    def __init__(self,base : int, alturea: int):
        super().__init__()
        self.__base=base
        self.__alturea=alturea
    def area(self):
        return self.__base * self.__alturea
    def __str__ (self):
        return f'Tu figura es un cuadrado con base: {self.__base} y altura: {self.__alturea}'
    
cuadrado= Cuadrado(7,1)
print(cuadrado.area())
print(cuadrado)