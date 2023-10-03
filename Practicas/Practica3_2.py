'''Practica numero 3 haciendo uso de Herencia y Polimorfismo

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 3
Fecha: 4/10/2023
'''
from abc import ABCMeta, abstractmethod

#Clase madre
class Mascota(metaclass=ABCMeta): 
    """Clase abstracta madre
    """
    def __init__(self, nombre: str, edad: int, duenio: str, tipo: str) -> None:
        """Constructor de la clase madre Mascota

        Args:
            nombre (str): Nombre de la mascota
            edad (int): Edad de la mascota
            duenio (str): Nombre del duenio
            tipo (str): Clasificacion de la mascota
        """
        
        '''Se inicilizan los atributos y asi solo para las clases que adjunten nuevos atributos'''
        self.__nombre = nombre
        self.__edad = edad
        self.__duenio = duenio
        self.__tipo = tipo
    
    #Getters y setters  (Encapsulamiento)
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre =nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad =edad
    
    @property
    def duenio(self):
        return self.__duenio
    @duenio.setter
    def duenio(self, duenio):
        self.__duenio =duenio
    
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo =tipo
    
    #Metodo habla
    @abstractmethod
    def habla(self):
        """Mostrara cuidados y caracteristicas dependiendo la clase haciendo una sobrecarga(Polimorfismo)
        """
        pass
    
    #Metodo tostring
    @abstractmethod
    def __str__(self) -> str:
        """Mostrara en consola los atributos caracteristicos de cada clase

        Returns:
            str: Retorna solo datos de tipo str
        """
        pass

class Domestica(Mascota, metaclass= ABCMeta):
    """Clase heradada con un atributo adicional 'ternura'
        (ABSTRACTA)

    Args:
        Mascota (class): Clase madre
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, ternura: int):
        """Constructor de la clase Domestica

        Args:
            ternura (int): numero de la ternura en escalra (1-10)
        """
        
        '''Se inicializan los atributos de la clase superior "Mascota" '''        
        Mascota.__init__(self, nombre, edad, duenio, tipo)
        self.__ternura = ternura
        
    #Getters y setters  (Encapsulamiento)
    @property
    def ternura(self):
        return self.__ternura
    @ternura.setter
    def ternura(self,ternura):
        self.__ternura =ternura
        
    #Metodo habla
    @abstractmethod
    def habla(self):
        pass

    #toString
    @abstractmethod
    def __str__(self) -> str:
        pass

class Exotica (Mascota, metaclass=ABCMeta) :
    """Clase heredada con un atributo adicional 'peligro'
        (ABSTRACTA)
    Args:
        Mascota (class): Clase madre
    """
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int):
        """Constructor de la clase heredada

        Args:
            peligro (int): Numero de peligro en un rango (1-10)
        """
        
        '''Se inicializan los atributos de la clase superior "Mascota" '''        
        Mascota.__init__(self, nombre, edad, duenio, tipo)
        self.__peligro = peligro
    
    #Getters y setters  (Encapsulamiento)
    @property
    def peligro(self):
        return self.__peligro
    @peligro.setter
    def peligro(self,peligro):
        self.__peligro = peligro
    
    #toString
    @abstractmethod
    def __str__(self) -> str:
        pass

    #Metodo habla
    @abstractmethod
    def habla(self):
        pass

#clase submadre Domestica
class Gato(Domestica):
    """Clase heredada
    
    Args:
        Domestica (class): Clase Domestica (submadre)
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, ternura: str) -> None:
        
        '''Se inicializa los atributos de la clase submadre (Domestica)'''
        Domestica.__init__(self, nombre, edad, duenio, tipo, ternura)
    
    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Miauw..."\n te hablare sobre mis cuidados...')
        print('>Comida deliciosa: ¡Necesito mi comida favorita y, de vez en cuando, un capricho especial como un poco de salmon o pollo!')
        print('>Mimos y caricias: Necesito que me mimen y acaricien con regularidad.')
        print('>Caja de arena impecable: Una caja de arena limpia, ¡no me gusta ensuciarme las patitas!')
        print('>Amor y atención constante: ¡Nada me hace mas feliz que sentirme amado y atendido por mi humano osea tu!')
        print('\n============================================================')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de ternura: {self.ternura}'

class Perro(Domestica):
    """Clase heredada

    Args:
        Domestica (class): Clase Domestica (submadre)
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, ternura: str):
        
        '''Se inicializa los atributos de la clase submadre (Domestica)'''
        Domestica.__init__(self, nombre, edad, duenio, tipo, ternura)
    
    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Gua..."\n te hablare sobre mis cuidados...')
        print('>Comida deliciosa y nutritiva: ¡Me encanta la comida! ')
        print('>Juegos y ejercicio: ¡Juega conmigo! Necesito correr, saltar y jugar para quemar energia y mantenerme feliz.')
        print('>Paseos emocionantes: Los paseos son lo mejor. Llevame a explorar el mundo exterior y a conocer a otros perros y personas.')
        print('>Amor y afecto: No puedo resistir un buen abrazo y caricias. ¡Dame mucho amor y atencion!')
        print('\n============================================================')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de ternura: {self.ternura}'

    
class Vivora(Exotica):
    """Clase heradada

    Args:
        Exotica (class): clase Exotica (submadre)
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int):
        
        '''Se inicializa los atributos de la clase submadre (Exotica)'''
        Exotica.__init__(self, nombre, edad, duenio, tipo, peligro)

    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Tsss..."\n te hablare sobre mis cuidados...')
        print('>Te recuerdo que puedo ser peligroso si tengo hambre, asi que no olvides alimentarme.')
        print('>Tenme lista una buena habit, quiero estar comodo')
        print('>Mudo de piel cada cierto tiempo, asi que tendras que limpiarlo')
        print('\n============================================================')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de peligro: {self.peligro}'

class Tigre(Exotica):
    """Clase heredada

    Args:
        Exotica (class): Clase Exotica (Submadre)
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int)-> None:
        
        '''Se inicializa los atributos de la clase submadre (Exotica)'''
        Exotica.__init__(self, nombre, edad, duenio,tipo, peligro)

    def habla(self)-> None:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Grrr..."\n te hablare sobre mis cuidados...')
        print('>Ahora que soy un cachorro necesito mucha comida, no olvides alimentarme o tendre que devorarte')
        print('>Mi habitad es lo mas importante, recuerda que crezco muy... rapido.')
        print('>Me tendras que enseñar a casar')
        print('\n============================================================')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de peligro: {self.peligro}'

    
class Dinosaurio(Exotica, metaclass=ABCMeta):
    """Clase heredada (EXOTICA) con un atributo adicional 'tipo_dinosaurio
        (ABSTRACTA)

    Args:
        Exotica (class): Clase Exotica (Submadre)
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int, tipo_dinosaurio: str)-> None:
        
        '''Se inicializan los atributos de la clase Exotica'''
        Exotica.__init__(self, nombre, edad, duenio, tipo, peligro)
        self.__tipo_dinosaurio = tipo_dinosaurio
        
    #Getters y setters  (Encapsulamiento)    
    @property
    def tipo_dinosaurio(self):
        return self.__tipo_dinosaurio
    @tipo_dinosaurio.setter
    def tipo_dinosaurio(self,tipo_dinosaurio):
        self.__tipo_dinosaurio = tipo_dinosaurio
        
    @abstractmethod
    def __str__(self) -> str:
        pass
#Subclasese de dinosaurio

class Brontosaurio(Dinosaurio):
    """Clase heredada

    Args:
        Dinosaurio (class): Clase heredada derivada de Exotica
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int, tipo_dinosaurio = 'Brontosaurio'):
       
        '''Se inicilizan los atributos de la clase dinosaurio'''
        Dinosaurio.__init__(self, nombre, edad, duenio,tipo, peligro, tipo_dinosaurio)
        
    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Sonido de Brontosaurio"\n te hablare sobre mis cuidados...')
        print('>Necesito mucho espacio, un parque del tamaño de un estadio estaria bien')
        print('>Demasiados arboles')
        print('\n============================================================')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de peligro: {self.peligro}\nTipo de dinosaurio: {self.tipo_dinosaurio}'


class Raptor(Dinosaurio):
    """Clase heredada

    Args:
        Dinosaurio (_type_): Clase heredada derivada de Exotica
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int, tipo_dinosaurio = 'Raptor'):
        Dinosaurio.__init__(self, nombre, edad, duenio, tipo, peligro, tipo_dinosaurio)

    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Sonido de Raptor"\n te hablare sobre mis cuidados...')
        print('>Tengo un metabolismo demesiado rapido...')
        print('>Necesito mucha comida y un espacio enorme')
        print('>Espero mis comodidas o te va ir mal jaja...')
        print('\n============================================================')       
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de peligro: {self.peligro}\nTipo de dinosaurio: {self.tipo_dinosaurio}'

class Trex(Dinosaurio):
    """Clase heredada

    Args:
        Dinosaurio (class): Clase heredada derivada de Exotica
    """
    
    def __init__(self, nombre : str, edad: int, duenio: str, tipo: str, peligro: int, tipo_dinosaurio='Trex') -> None:
        Dinosaurio.__init__(self, nombre, edad, duenio, tipo, peligro, tipo_dinosaurio)
        
    def habla(self)-> str:
        print('\n============================================================')
        print('Hola yo soy tu nueva mascoata "Sonido de Trex"\n te hablare sobre mis cuidados...')
        print('>No hace falta decir que soy imponente, asi que mejor dame un espacio solo para mi')
        print('>Mucha comida por cierto')
        print('>Espero no verte cuando este hambriento')
        print('\n============================================================')
        
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} meses\nDuenio: {self.duenio}\nTipo: {self.tipo}\nFactor de peligro: {self.peligro}\nTipo de dinosaurio: {self.tipo_dinosaurio}'