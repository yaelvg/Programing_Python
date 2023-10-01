class Alumno():
    """Contiene atributos de un alumno"""    
    boleta=''
    nombre=''
    def hablar(self):
        """Presentacion del alumno
        """
        print(f'Hola soy {self.nombre} \nMi boleta {self.boleta}')

alumno1=Alumno() #Objeto...
alumno1.nombre='Adan'
alumno1.boleta='12345'
alumno1.hablar()
alumno2=Alumno() #Objeto...
alumno2.nombre='Ale'
alumno2.boleta='234'
alumno2.hablar()
class B:
    def __str__(self) -> str:
        t=12
        print(t)
x=B()
print(x)