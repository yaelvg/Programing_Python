from PyQt6 import QtCore, QtGui
from Ui_calculadora import *
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtGui import QKeyEvent
from Ui_ayuda import *
import sys
import math


class MainWindow(QMainWindow, Ui_MainWindow):
    """Clase que contiene todos las caracteristicas y 
    funciones de la interfase
    """
    
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.__internal_str = "0"
        
        # AC
        self.pushButton_27.clicked.connect(self.limpieza)
        #C
        self.pushButton_26.clicked.connect(self.limpieza_2)
        
        # Numeros
        self.pushButton.clicked.connect(self.numberPressed)
        self.pushButton_4.clicked.connect(self.numberPressed)
        self.pushButton_5.clicked.connect(self.numberPressed)
        self.pushButton_6.clicked.connect(self.numberPressed)
        self.pushButton_8.clicked.connect(self.numberPressed)
        self.pushButton_9.clicked.connect(self.numberPressed)
        self.pushButton_10.clicked.connect(self.numberPressed)
        self.pushButton_11.clicked.connect(self.numberPressed)
        self.pushButton_12.clicked.connect(self.numberPressed)
        self.pushButton_13.clicked.connect(self.numberPressed)
        self.pushButton_25.clicked.connect(self.factorial)

        
        # Punto
        self.pushButton_2.clicked.connect(self.punto_decimal)
        
        #Operaciones
        self.pushButton_15.clicked.connect(self.numberPressed)
        self.pushButton_7.clicked.connect(self.numberPressed)
        self.pushButton_14.clicked.connect(self.operator_2)
        self.pushButton_16.clicked.connect(self.numberPressed)
        self.pushButton_17.clicked.connect(self.ayuda)
        self.pushButton_18.clicked.connect(self.raiz)
        self.pushButton_28.clicked.connect(self.operador)
        self.pushButton_29.clicked.connect(self.numberPressed)
        self.pushButton_21.clicked.connect(self.logaritmo)
        self.pushButton_22.clicked.connect(self.seno)
        self.pushButton_23.clicked.connect(self.coseno)
        self.pushButton_24.clicked.connect(self.tangente)
        self.pushButton_30.clicked.connect(self.cuadrado)
        self.pushButton_31.clicked.connect(self.inverso)
        
        #PI
        self.pushButton_19.clicked.connect(self.pi)
        #e
        self.pushButton_20.clicked.connect(self.e)
        #Resultado
        self.pushButton_3.clicked.connect(self.evaluator)
        



    def ayuda(self):
        """Abre otra ventana que contienen indicaciones 
        de como usar la calculadora
        """
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_ayuda_2()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def limpieza(self):
        """Limpieza total
        """
        self.__internal_str = "0"
        self.setRichText("0")
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() >= QtCore.Qt.Key.Key_0 and event.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(str(event.key() - 48)) # key_0 es igual a 48
        if event.key() == QtCore.Qt.Key.Key_Period: # Punto decimal
            self.decimal_point()
            
    def numberPressed(self):
        """Proporciona el numero o dato asociado con el widget
        """
        number = self.sender().text()
        self.setNumber(number)
        
        
    def punto_decimal(self):
        x=self.label.text()
        if x == '0':
            self.__internal_str = "."
            self.setRichText(self.__internal_str) # Con texto con formato

        else:
           self.__internal_str =x + "."
           self.setRichText(self.__internal_str)

    def setNumber(self, number: str):
        """Coloca el pantalla el numro que digito el usuario

        Args:
            number (str): Numero que digito
        """
        self.__internal_str += number
        self.__internal_str = self.number2string(self.__internal_str)
        self.setRichText(self.__internal_str) # Con texto con formato
   
    def number2string(self, num: str) -> str:
        """Converts a number to a string

        Args:
            num (str): Numero escrito por el usuario

        Returns:
            str: 
        """
        try:
            number = float(num)
            if number.is_integer():
                return str(int(number))
            else:
                return str(number)
        except:
            return str(num) 
        
    def setRichText(self, number: str):
        """Se encarga de colocarlo en pantalla
        """
        
        #self.label.setText(f"<html><head/><body><p align=\"right\">{number}</p></body></html>")
        self.label.setText(f"{number}")
    
   
    def pi(self):
        x=self.label.text()
        print(x)
        
        if x == '0':
            self.__internal_str = "3.14159"
            self.setRichText(self.__internal_str) # Con texto con formato

            
        else:
           self.__internal_str =x + "3.14159"
           self.setRichText(self.__internal_str)
           
           
    def e(self):
        x=self.label.text()
        print(x)
        
        if x == '0':
            self.__internal_str = "2.71828"
            self.setRichText(self.__internal_str) 

            
        else:
           self.__internal_str =x + "2.71828"
           self.setRichText(self.__internal_str)
           
           
    def operador(self):
        x=self.label.text()
        print(x)
        
        if x == '0':
            self.__internal_str = "("
            self.setRichText(self.__internal_str)

        else:
           self.__internal_str =x + "("
           self.setRichText(self.__internal_str)
           
         
    def evaluator(self):
        """Evalua cada operacion que se encuentre en  la etiqueta
        """
        try:
            x=self.label.text()
            ans=eval(x)
            self.setRichText(ans)
        except:
            self.setRichText('ERROR')
            
    def limpieza_2(self):
        """Elima el ultimo termino escrito por el usuario
        """
        x=self.label.text()
        y=len(x)-1
        window.limpieza()
        x=x[0:y]
        self.__internal_str =x + ""
        self.setRichText(self.__internal_str)
                    
    def operator_2(self):
        x=self.label.text()
        print(x)
        
        if x == '0':
            self.__internal_str = "-"
            self.setRichText(self.__internal_str) 

        else:
           self.__internal_str =x + "-"
           self.setRichText(self.__internal_str)
           
    def factorial(self):
        """Genera factorial 
        """
        n=self.label.text()
        try:
            n=int(n)
            n= math.factorial(n)
            self.setRichText(n)

        except:
            self.setRichText('ERROR')
    
    def logaritmo(self):
        """Genera logaritmo del numero
        """
        n=self.label.text()
        try:
            n=float(n)
            n= math.log(n)
            self.setRichText(n)

        except:
            self.setRichText('ERROR')
            
    def seno(self):
        """Seno en grado
        """
        n=self.label.text()
        try:
            n=float(n)
            n= math.sin(math.radians(n))
            self.setRichText(n)

        except:
            self.setRichText('ERROR')  
            
    def coseno(self):
        """Coseno en grados
        """
        n=self.label.text()
        try:
            n=float(n)
            n= math.cos(math.radians(n))
            self.setRichText(n)

        except:
            self.setRichText('ERROR') 
            
    def tangente(self):
        """Tangente en grados
        """
        n=self.label.text()
        try:
            n=float(n)
            n= math.tan(math.radians(n))
            self.setRichText(n)

        except:
            self.setRichText('ERROR') 
            
    def cuadrado(self):
        """Eleva al cuadrado
        """
        n=self.label.text()
        try: 
            n=float(n)
            n= math.pow(n,2)
            self.setRichText(n)
        except:
            self.setRichText('ERROR') 

    def inverso(self):
        """Inverso de un numero
        """
        n=self.label.text()
        try: 
            n=float(n)
            n= math.pow(n,-1)
            self.setRichText(n)
        except:
            self.setRichText('ERROR')
            
    def raiz(self):
        """Genera la raiz cuadrada del numero escrito
        """
        n=self.label.text()
        try: 
            n=float(n)
            n= math.sqrt(n)
            self.setRichText(n)
        except:
            self.setRichText('ERROR')  
    


'''Principal'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.limpieza()
    sys.exit(app.exec())