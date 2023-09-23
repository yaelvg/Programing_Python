
import os

class Profesor():
    
    def __init__(self, nombre_profesor : str, n_empleado : str) -> None:
        self.__nombre_profesor = nombre_profesor
        self.__n_empleado = n_empleado

    @property
    def nombre_profesor(self):
        return self.__nombre_profesor
    @nombre_profesor.setter
    def nombre_profesor(self,nombre_profesor):
        self.__nombre_profesor = nombre_profesor
        
    @property
    def n_empleado(self):
        return self.__n_empleado
    @n_empleado.setter
    def n_empleado(self,n_empleado):
        self.__n_empleado = n_empleado
        
        
class Alumno():
    
    def __init__(self, nombre : str, apellidop : str, apellidom: str, nboleta: int, dia: int,
                 mes: int, año: int, carrera: str, grupo: str, correo: str) -> None:
        self.__nombre = nombre
        self.__apellidop =apellidop
        self.__apellidom =apellidom
        self.__nboleta = nboleta
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        self.__carrera = carrera
        self.__grupo = grupo
        self.__correo = correo
        
    #Setters y getters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def apellidop(self):
        return self.__apellidop
    @apellidop.setter
    def apellidop(self,apellidop):
        self.__apellidop = apellidop
 
    @property
    def apellidom(self):
        return self.__apellidom
    @apellidom.setter
    def apellidom(self,apellidom):
        self.__apellidom = apellidom       

    @property
    def nboleta(self):
        return self.__nboleta
    @nboleta.setter
    def nboleta(self,nboleta):
        self.__nboleta = nboleta
        
    @property
    def dia(self):
        return self.__dia
    @dia.setter
    def dia(self,dia):
        self.__dia = dia 

    @property
    def mes(self):
        return self.__mes
    @mes.setter
    def mes(self,mes):
        self.__mes = mes  

    @property
    def año(self):
        return self.__año
    @año.setter
    def año(self,año):
        self.__año = año  
        
    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def carrera(self,carrera):
        self.__carrera = carrera
        
    @property
    def grupo(self):
        return self.__grupo
    @grupo.setter
    def grupo(self,grupo):
        self.__grupo = grupo

    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,correo):
        self.__correo = correo    
class Lista():
    
    def __init__(self) -> None:
        self.__profesor= None
        self.__lista = []
    
    def registro_profesor(self, nombre: str, numero: int) -> None:
        self.__profesor= Profesor(nombre,numero)
    
    def registro_alumnos(self, alumno: Alumno = None, nombre: str = None, apellidop: str = None, apellidom: str = None ,nboleta: int = None,
                         dia: int = None, mes: int = None, año: int = None, carrera: str = None, grupo: str = None, correo: str = None) -> None:
        if alumno is not None:
            self.__lista.append(alumno)
        else:
            alumno = Alumno(nombre, apellidop, apellidom, nboleta, dia, mes, año, carrera, grupo, correo)
            self.__lista.append(alumno)
        
    def impresion(self) -> None:
        print(f'Profesor: {self.__profesor.nombre_profesor}')
        print(f'No. Empleado: {self.__profesor.n_empleado}')
        print('================================================================')
        print('\t\tLista de Alumnos Inscritos')
        print('================================================================') 
        cont=1   
        for alumno in self.__lista:
            print(f'{cont} {alumno.apellidop} {alumno.apellidom}, {alumno.nombre} - {alumno.nboleta} - {alumno.dia}/{alumno.mes}/{alumno.año} - \n {alumno.carrera} - {alumno.grupo} - {alumno.correo}.')
            cont+=1
        print('================================================================') 
        print(f'Total de alumnos: {len(self.__lista)}.')

def registros():
    
    i=0
    while True:
        
        if i == 0:
            print('\n\n********************')
            print('Datos del profesor')
            nombre=input('Nombre Completo:')
            nempleado=int(input('Numero de empleado: '))
            lista_alumnos.registro_profesor(nombre, nempleado)
            print('********************')
            print('\n\n////////////////////////////////')
            print('\n Datos de Alumnos')
            
        print(f'Alumnno {i+1}')
        apellidop=input('Apellido paterno:')
        apellidom=input('Apellido materno:')
        a_nombre=input('Nombre:')
        nboleta=int(input('Numero de boleta: '))
        dia=int(input('Día de nacimiento: '))
        mes=int(input('Mes de nacimiento: '))
        año=int(input('Año de nacimiento: '))
        carrera=input('Carrera:')
        grupo=input('Grupo:')
        correo=input('Correo:')
        print('\n')
        i+=1
        
        lista_alumnos.registro_alumnos(alumno = Alumno(a_nombre,apellidop,apellidom,nboleta,dia,mes,año,carrera,grupo,correo))
        
        x=input('Desea agregar mas alumnos: Sí "1", No "0": ')
        if x == '0': break
        
        
lista_alumnos= Lista()
registros()
os.system('cls')
lista_alumnos.impresion()
