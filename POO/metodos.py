class Alumno:
    var= 'Holaa desde una variable de clase'
    @classmethod
    def di_hola(cls) -> str: #Metodo de clase
        return cls.var
    @staticmethod
    def di_hola_estatico() -> str : #Metodo estatico
        return 'HOLI'
        
    def __init__(self, nombre: str, cuenta: int): #Metodo de instancia
        #Varibles de instancia
        self.nombre= nombre
        self.cuenta= cuenta
        #funciones de instancia para eso es el uso del self
    def habla(self) -> str:
        return 'Hola'
#print(Alumno.habla())
print(Alumno.di_hola())
        