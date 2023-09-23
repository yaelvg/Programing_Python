'''No esta este concepto en python  pero se notifican con _ a los protegidos 
y a los privados  con __'''
#Todos los atributos son publicos en python
#El encapsulamiento me dice que todos los atributos deben ser privados o por lo menos protegidos
class Alumnos():
    
    def __init__(self, nombre, cuenta) -> None:
        self.__nombre = nombre
        self.__cuenta = cuenta
        
    def __str__(self) -> str:
        return f'Hola mi nombre es {self.__nombre}\n Cuenta: {self.__cuenta}'
    
    @property
    #getter
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, cambio : str):
        self.__nombre = cambio
        
alumno1=Alumnos('xxx', '')

#No sirve hacer lo siguiente ya que las variables son privadas
alumno1.__nombre='aleee'
alumno1.__cuenta='1232'
print(alumno1)
print('\n\n')
alumno1.nombre='Aleee'
print(alumno1)
print(f'El nombre del alumno es {alumno1.nombre}')