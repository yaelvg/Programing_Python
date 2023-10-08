'''Examen_1 Parte 1.'''

class Pelicula():
    """Clase Pelicula cuenta con los atributos pricipales de una pelicula
    """
    def __init__(self, titulo: str, anio: int, duracion: float, clasificar: str, director: str, actores: str, descripcion: str):
        """Constructor de clase

        Args:
            titulo (str): Titulo de la pelicula
            anio (int): año de estreno
            duracion (float): duracion de la pelicula
            clasificar (str): clasificacion de la pelicula
            director (str): director de la pelicula
            actores (str): actores pricipales de la pelicula
            descripcion (str): breve descripcion de la pelicula
        """
        self.__titulo=titulo
        self.__anio=anio
        self.__duracion=duracion
        self.__clasificar=clasificar
        self.__director=director
        self.__actores=actores
        self.__descripcion=descripcion
    
    #Getters y setter Encapasulamiento
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo=titulo
        
    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self, anio):
        self.__anio=anio

    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion=duracion
        
    @property
    def clasificar(self):
        return self.__clasificar
    @clasificar.setter
    def clasificar(self, clasificar):
        self.__clasificar=clasificar

    @property
    def director(self):
        return self.__director
    @director.setter
    def director(self, director):
        self.__director=director

    @property
    def actores(self):
        return self.__actores
    @actores.setter
    def actores(self, actores):
        self.__actores=actores

    @property
    def descripcion(self):
        self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion=descripcion
        
    def __str__(self):
        """Me retorna los atributos de la clase
        """
        return f'Titulo: {self.__titulo}\nAnio: {self.__anio}\nDuracion: {self.__duracion}\n Clasificar: {self.__clasificar}\nDirector: {self.__director}\nActores: {self.__actores}\nDescripcion: {self.__descripcion}\n'


class Catalogo():
    """Me permite observar todas las peliculas que se vayan creando
    """
    
    def __init__(self) -> None:
        """Constructor de clase"""
        #Lista que almacenara cada pelicula creada 
        self.__lista= list()

    def pelicula(self,titulo: str = None, anio: int = None,duracion: float = None, clasificar: str = None, director: str = None, actores: list = None, descripcion: str = None):
        """Crea las instancias de la clase Pelicula.
        """
        pelicula= Pelicula(titulo,anio,duracion,clasificar, director, actores, descripcion)
        self.__lista.append(pelicula)
        
    def impresion(self):
        """Imprime todas las instancias almacenadas en el atributo pelicula
        """
        for numero, peli in enumerate(self.__lista):
            print(f'Pelicula [{numero}]')
            print(peli)
        