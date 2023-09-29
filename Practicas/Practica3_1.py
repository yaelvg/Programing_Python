'''Practica numero 3 haciendo uso de Herencia y Polimorfismo

Nombre: Yael Alejandro Valdez Gonzalez
Boleta: 2022640608
Practica 3
Fecha: 4/10/2023
'''
#Clase madre
class Computadora:
    
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str) -> None:
        """_summary_

        Args:
            memoria (str): ...
            procesador (str): ...
            almacenamiento (str): ...
            gpu (str): ...
        """
        self.__memoria = memoria
        self.__procesador = procesador
        self.__almacenamiento = almacenamiento
        self.__gpu = gpu
        
    #Getters y setters
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
    
class ComputadoraPortatil (Computadora):
    
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, pulgadas : int, n_puertos: str):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__pulgadas = pulgadas
        self.__n_puertos = n_puertos
    
    #Getters y setters
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
            
    #Metodo
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora Portatil:')
        print(f'Memoria RAM: {self.__memoria} GB')
        print(f'Procesador: {self.__procesador}')
        print(f'Almacenamiento (interno): {self.__almacenamiento} GB')
        print(f'GPU: {self.__gpu}')
        print(f'Tamaño de pantalla: {self.__pulgadas} pulgadas')
        print(f'Número de puertos: {self.__n_puertos}')

class ComputadoraEscritorio (Computadora):
    """Clase ComputadoraEscritorio heradada 

    Args:
        Computadora (class): Clase madre
    """
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, peso: float, largo: float, ancho : float) -> None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__peso = peso
        self.__largo = largo
        self.__ancho = ancho    
    #getters y setters
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
        
    #Metodo
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora de Escritorio:')
        print(f'Memoria RAM: {self.__memoria} GB')
        print(f'Procesador: {self.__procesador}')
        print(f'Almacenamiento (interno): {self.__almacenamiento} GB')
        print(f'GPU: {self.__gpu}')
        print(f'Peso: {self.__peso} kg')
        print(f'largo: {self.__largo}')    
        print(f'ancho: {self.__ancho}')    
     
        
    
class TelefonoInteligente (Computadora):
    """Clase TelefonoInteligente heredada

    Args:
        Computadora (class): Clase madre
    """
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, sistema_op: str , color: str, marca: str) -> None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__sistema_op = sistema_op
        self.__color = color
        self.__marca = marca
        
    #Getters y setters
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
    
    #Metodo
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tTelefono Inteligente:')
        print(f'Memoria RAM: {self.__memoria} GB')
        print(f'Procesador: {self.__procesador}')
        print(f'Almacenamiento (interno): {self.__almacenamiento} GB')
        print(f'GPU: {self.__gpu}')
        print(f'Sistema Operativo: {self.__sistema_op}')
        print(f'Color: {self.__color}')    


class Tablet (Computadora):
    """Clase Tablet heredada

    Args:
        Computadora (class): Clase madre
    """
    def __init__(self,memoria: str, procesador: str, almacenamiento: str, gpu: str, accesorios: list, garantia: str ):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__acesorios = accesorios
        self.__garantia = garantia
    
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
    
    #Metodos
    def caracteristicas(self):
        print('\n\t\t********Factura********\n')
        print('\tComputadora de Escritorio:')
        print(f'Memoria RAM: {self.__memoria} GB')
        print(f'Procesador: {self.__procesador}')
        print(f'Almacenamiento (interno): {self.__almacenamiento} GB')
        print(f'GPU: {self.__gpu}')
        print(f'Accesorios: {self.__acesorios}')
        print(f'Garantia: {self.__garantia}')    
