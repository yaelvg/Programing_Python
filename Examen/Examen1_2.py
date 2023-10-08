
class Contacto():
    """Clase que contiene los atributos principales
    """
    def __init__(self, nombre: str, numero: int) -> None:
        """constructor de clase

        Args:
            nombre (str): Nombre del contacto
            numero (int): numero del contacto
        """
        self.__nombre = nombre
        self.__numero = numero

    #Getters y setter Encapasulamiento
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def __str__(self) -> str:
        return f'Nombre: {self.__nombre}\nNumero: {self.__numero}\n'
    
class Agenda():
    """Clase que contiene todas las intancias creadas de la clase Constacto
    """
    
    def __init__(self) -> None:
        """Constructor de clase
        """
        #contien instancias de Constacto
        self.__lista = list()
    
    def registros(self, nombre: str, numero: int):
        """Crea la instancia de tipo contacto

        Args:
            nombre (str): Nombre del contacto
            numero (int): Numero del contacto.
        """
        #Se crea la instancia y despues se almacena en la lista
        contacto= Contacto(nombre, numero)
        self.__lista.append(contacto)
        
    def contactos(self):
        """Muestra los contactos
        """
        for numero, contacto in enumerate(self.__lista):
            print(f'Numero[{numero+1}]')
            print(contacto)
    
    def eliminar(self, indice: int):
        """Elimina los contactos

        Args:
            indice (int): Indice del contacto
        """
        self.__lista.pop(indice-1)
    
    def busqueda_numero(self, numero):
        """Realiza una busqueda por numero

        Args:
            numero (int): numero del contacto
        """
        x=0
        for contacto in self.__lista:
            if contacto.numero == numero:
                print(contacto)
        if x == 0:
            print('Datos no encontrados')
    
    def busqueda_nombre(self, nombre: str):
        """Realiza una busqueda por nombre

        Args:
            nombre (str): Nombre del contacto
        """
        x=0
        for contacto in self.__lista:
            if contacto.nombre == nombre:
                print(contacto)
                x=1
        if x == 0:
            print('Datos no encontrados')
                
                
