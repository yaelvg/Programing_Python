'''Practica numero 3 haciendo uso de Herencia y Polimorfismo

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 3
Fecha: 4/10/2023
'''
from abc import ABCMeta, abstractmethod

#Clase madre
class Computadora(metaclass=ABCMeta):
    """Clase abstracta Madre
    """
    
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str) -> None:
        """Constructor de clase Computadora

        Args:
            memoria (str):Tipo y cantidad de memoria  que tendra cada instancia de la subclase
            procesador (str):Tipo procesador que tendra cada instancia de la subclase
            almacenamiento (str):Tipo y cantidad de almacenamiento que tendra cada instancia de la subclase
            gpu (str): Tipo de GPU que tendra cada instancia de la subclase
        """
        
        '''Se inicilizan los atributos y asi solo para las clases que adjunten nuevos atributos'''
        self.__memoria = memoria
        self.__procesador = procesador
        self.__almacenamiento = almacenamiento
        self.__gpu = gpu
        
    #Getters y setters  (Encapsulamiento)
    @property
    def memoria(self):
        return self.__memoria
    @memoria.setter
    def memoria(self,memoria):
        self.__memoria = memoria
    
    @property
    def procesador(self):
        return self.__procesador
    @procesador.setter
    def procesador(self,procesador):
        self.__procesador = procesador
    
    @property
    def almacenamiento(self):
        return self.__almacenamiento
    @almacenamiento.setter
    def almacenamiento(self,almacenamiento):
        self.__almacenamiento = almacenamiento
    
    @property
    def gpu(self):
        return self.__gpu
    @gpu.setter
    def gpu(self,gpu):
        self.__gpu = gpu
    
    @abstractmethod
    def caracteristicas(self):
        """Muestra las caracteristicas de cada intancia, las cuales con los atributos de la
        clase madre abstracta. 
        """
        print('\n\t\t********Factura********\n')
        print('\tComputadora Portatil:')
        print(f'Memoria RAM: {self.memoria} GB')
        print(f'Procesador: {self.procesador}')
        print(f'Almacenamiento (interno): {self.almacenamiento} GB')
        print(f'GPU: {self.gpu}')
        print(f'Tamaño de pantalla: {self.__pulgadas} pulgadas')
        print(f'Número de puertos: {self.__n_puertos}')
    
class ComputadoraPortatil (Computadora):
    """Clase heredada con 2 atributos adicionales 'n_puertos' y 'pulgadas'

    Args:
        Computadora (class): Clase Madre
    """
    
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, pulgadas : int, n_puertos: str):
        """Constructor de clase ComputadoraPortatil

        Args:
            pulgadas (int): numero de pulgadas de la instancia
            n_puertos (str): numero de puertos de la instancia
        """
        '''Se inicializan los atributos de la clase superior "Computadora" '''
        Computadora.__init__(self, memoria, procesador, almacenamiento, gpu)
        self.__pulgadas = pulgadas
        self.__n_puertos = n_puertos
    
    #Getters y setters  (Encapsulamiento)
    @property
    def pulgadas(self):
        return self.__pulgadas
    @pulgadas.setter
    def pulgadas(self,pulgadas):
        self.__pulgadas = pulgadas
    
    @property
    def n_puertos(self):
        return self.__n_puertos
    @n_puertos.setter
    def n_puertos(self, n_puertos):
        self.__n_puertos = n_puertos
            
    #Sobrecarga de metodos
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora Portatil:')
        print(f'Memoria RAM: {self.memoria} GB')
        print(f'Procesador: {self.procesador}')
        print(f'Almacenamiento (interno): {self.almacenamiento} GB')
        print(f'GPU: {self.gpu}')
        print(f'Tamaño de pantalla: {self.__pulgadas} pulgadas')
        print(f'Número de puertos: {self.__n_puertos}')

class ComputadoraEscritorio (Computadora):
    """Clase heradada con 3 atributos adicionales 'peso', 'largo' y 'ancho'

    Args:
        Computadora (class): Clase Madre
    """
    def __init__(self, memoria: str, procesador: str, almacenamiento: str, gpu: str, peso: float, largo: float, ancho : float) -> None:
        """Constructor de clase ComputadoraEscritorio

        Args:
            peso (float): Peso de la instancia
            largo (float): largo de la instancia
            ancho (float): ancho de la instancia
        """
        
        '''Se inicializan los atributos de la clase superior "Computadora" '''
        Computadora.__init__(self,memoria, procesador, almacenamiento, gpu)
        self.__peso = peso
        self.__largo = largo
        self.__ancho = ancho    
        
    #Getters y setters  (Encapsulamiento)
    @property
    def precio(self):
        return self.__peso
    @precio.setter
    def peso(self, peso):
        self.__peso = peso
    
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho
    
    @property
    def largo(self):
        return self.__largo
    @largo.setter
    def largo(self, largo):
        self.__largo = largo
        
    #Sobrecarga de metodos
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora de Escritorio:')
        print(f'Memoria RAM: {self.memoria} GB')
        print(f'Procesador: {self.procesador}')
        print(f'Almacenamiento (interno): {self.almacenamiento} GB')
        print(f'GPU: {self.gpu}')
        print(f'Peso: {self.__peso} kg')
        print(f'largo: {self.__largo}')    
        print(f'ancho: {self.__ancho}')    
          
class TelefonoInteligente (Computadora):
    """Clase heredada con 2 atributos adicionales 'sistema_op', 'color', 'marca'.

    Args:
        Computadora (class): Clase madre
    """
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, sistema_op: str , color: str, marca: str) -> None:
        """Constructor de Clase TelefonoInteligente

        Args:
            sistema_op (str): Sistema operativo de la instacia
            color (str): Color caracteristico de la instencia
            marca (str): Marca de la instencia
        """
        
        '''Se inicializan los atributos de la clase superior "Computadora" '''
        Computadora.__init__(self,memoria, procesador, almacenamiento, gpu)
        self.__sistema_op = sistema_op
        self.__color = color
        self.__marca = marca
        
    #Getters y setters  (Encapsulamiento)
    @property
    def sistema_op(self):
        return self.__sistema_op
    @sistema_op.setter
    def sistema_op(self,sistema_op):
        self.__sistema_op = sistema_op
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color = color
    
    #Sobrecarga de metodos

    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tTelefono Inteligente:')
        print(f'Memoria RAM: {self.memoria} GB')
        print(f'Procesador: {self.procesador}')
        print(f'Almacenamiento (interno): {self.almacenamiento} GB')
        print(f'GPU: {self.gpu}')
        print(f'Sistema Operativo: {self.__sistema_op}')
        print(f'Color: {self.__color}')    

class Tablet (Computadora):
    """Clase heredada con 2 atributos adicionales 'accesorios' y 'garantia'

    Args:
        Computadora (class): Clase madre
    """
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, accesorios: list, garantia: str ):
        """Constructor de la clase Tablet

        Args:
            accesorios (list): Accesorios que tendra la instancia
            garantia (str): Garantia en años o meses de la instancia
        """
    
        '''Se inicializan los atributos de la clase superior "Computadora" '''    
        Computadora.__init__(self, memoria, procesador, almacenamiento, gpu)
        self.__acesorios = accesorios
        self.__garantia = garantia
    
    #Getters y setters  (Encapsulamiento)
    @property
    def accesorios(self):
        return self.__acesorios
    @accesorios.setter
    def accesorios(self, accesorios):
        self.__acesorios = accesorios

    @property
    def garantia(self):
        return self.__garantia
    @garantia.setter
    def garantia(self, garantia):
        self.__garantia = garantia
    
    #Sobrecarga de metodos
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora de Escritorio:')
        print(f'Memoria RAM: {self.memoria} GB')
        print(f'Procesador: {self.procesador}')
        print(f'Almacenamiento (interno): {self.almacenamiento} GB')
        print(f'GPU: {self.gpu}')
        print(f'Accesorios: {self.__acesorios}')
        print(f'Garantia: {self.__garantia}')   
        
        
        
'''Principal'''
#Instancias de tipo computadora portatil incializadas
lap_a=ComputadoraPortatil(' DDR4 8GB RAM',' Intel Core i5-11600K','Samsung 970 EVO Plus 1TB NVMe SSD','NVIDIA GeForce RTX 3080','13',5)
lap_b=ComputadoraPortatil('Corsair Vengeance LPX 16GB DDR4 RAM','AMD Ryzen 7 5800X','Western Digital WD Black 4TB HDD','AMD Radeon RX 6800 XT','14',5)
lap_c=ComputadoraPortatil('Kingston HyperX Fury 32GB DDR4 RAM','Western Digital WD Black 4TB HDD','Crucial MX500 500GB SATA SSD','Integrated Intel Iris Xe Graphics','15',7)

#Instancias de computadora de Escritorio incializadas
compu_a=ComputadoraEscritorio('DDR4 8GB','AMD Ryzen 5 5600X','Kingston SNV2S/1000G 1TB','NVIDIA GeForce RTX 3080',1.1,20.9,10.7)
compu_b=ComputadoraEscritorio('DDR4 16GB','Intel Core i7-10700K','Samsung 970 EVO NVMe SSD','Nvidia Evga SC RTX 20 Series RTX 2060 06G-P4-2062-KR 6GB',1.3,18.0,8.0)
compu_c=ComputadoraEscritorio('DDR4 32GB','AMD Ryzen 3 3300X','Western Digital Purple Wd10purz 1TB','Nvidia PNY Quadro Series P620',1.6,19.5,11.2)

#Instancias de Telefono inteligente
tel_a=TelefonoInteligente('8 RAM','xxx','32','xx','IOS','Rojo', 'Apple')
tel_b=TelefonoInteligente('12 RAM','xxx','64','Adreno 660','Android','Negro','Xiomi')
tel_c=TelefonoInteligente('12 RAM','xxx','128','Adreno 660','Android','Azul','Sony')

#Instancias de tablet incializadas
tablet_a=Tablet('4 RAM','ARM','16','XX',['Teclado','Lapiz','Bocina'],'3 meses')
tablet_b=Tablet('8 RAM','Intel ATOM','64','Adreno 640',['Funda', 'Lapiz','Audifonos'],'8meses')
tablet_c=Tablet('8 RAM','Intel Core','128','Nvidia',['Lapiz','smartwatch'],'1 año')


#Llamado de metodos
lap_a.caracteristicas()
compu_b.caracteristicas()
tel_c.caracteristicas()
tablet_a.caracteristicas()