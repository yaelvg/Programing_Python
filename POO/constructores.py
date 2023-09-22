#Uso del init para el uso de inicializar un objeto.
class Alumno():
    """Contiene atributos de un alumno"""    
    boleta=''
    nombre=''
    edad = 0
    def __init__(self, nombre: str, boleta: int, edad=0):
        self.nombre= nombre
        self.boleta= boleta
        self.edad= edad
    def __str__(self) -> str:
        return f'Hola soy {self.nombre} \nMi boleta {self.boleta}\n y mi edad es {self.edad}'
    
    def hablar(self):
        """Presentacion del alumno
        """
        print(f'Hola soy {self.nombre} \nMi boleta {self.boleta}\n y mi edad es {self.edad}')
        
alumno1=Alumno(nombre='Ale',boleta='1231')
alumno1.hablar()
'''Para el uso de la sobrecargar de contructores en python no se puede, se utilizan las varaiables 
opcionales'''
#Uso del la funcion str, retora una cadena de texto
print('\n\n Uso del __str__')
print(alumno1)