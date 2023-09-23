#Uso del init para el uso de inicializar un objeto.
class Alumno():
    """Contiene atributos de un alumno"""    
    #boleta=''
    #nombre=''
    #edad = 0
    
    def __init__(self, nombre: str, boleta: int, edad: int):
        self.nombre= nombre
        self.boleta= boleta
        self.edad= edad
        
    def __str__(self) -> str:
        return f'Hola soy {self.nombre} \nMi boleta {self.boleta}\n y mi edad es {self.edad}'
    
    def hablar(self):
        """Presentacion del alumno
        """
        print(f'Hola soy {self.nombre} \nMi boleta {self.boleta}\n y mi edad es {self.edad}')
        
#Variables de clase que no pertenecen a una instancia, evitar el uso de varibles globales
#print(Alumno.edad)
#Variables de intancia es con el uso de los contructores. para eso se hace la creacion de un alumno
alumno1=Alumno('Ale','12031',20)
print(alumno1)
