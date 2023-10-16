import typing
from PyQt6 import QtCore, QtGui
from Ui_calculadora import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QWidget
from PyQt6.QtGui import QKeyEvent
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.__internal_str = "0"
        
        # AC
        self.pushButton_27.clicked.connect(self.clear)
        
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
        # Punto
        self.pushButton_2.clicked.connect(self.decimal_point)
        #Operaciones
        self.pushButton_15.clicked.connect(self.multiplicar)
        self.pushButton_7.clicked.connect(self.sumar)
        self.pushButton_14.clicked.connect(self.restar)
        self.pushButton_16.clicked.connect(self.division)
        self.pushButton_28.clicked.connect(self.p_izquierdo)
        self.pushButton_29.clicked.connect(self.p_derecho)



        
        
    def clear(self):
        self.__internal_str = "0"
        self.setRichText("0")
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() >= QtCore.Qt.Key.Key_0 and event.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(str(event.key() - 48)) # key_0 es igual a 48
        if event.key() == QtCore.Qt.Key.Key_Period: # Punto decimal
            self.decimal_point()
            
    def numberPressed(self):
        number = self.sender().text()
        self.setNumber(number)
        
    def decimal_point(self):
        if self.__internal_str.find(".") == -1:
            self.__internal_str +=  "."
         
    def setNumber(self, number: str):
        self.__internal_str += number
        self.__internal_str = self.number2string(self.__internal_str)
        self.setRichText(self.__internal_str) # Con texto con formato
   
    def number2string(self, num: str) -> str:
        try:
            number = float(num)
            if number.is_integer():
                return str(int(number))
            else:
                return str(number)
        except:
            return num 
        
    def setRichText(self, number:str):
        self.label.setText(f"<html><head/><body><p align=\"right\">{number}</p></body></html>")
    
    def multiplicar(self):
        txt=self.label.text()
        self.setRichText('*')
            
    def division(self):
        if self.__internal_str.find("/") == -1:
            self.__internal_str +=  "/"
            
    def sumar(self):
        if self.__internal_str.find("+") == -1:
            self.__internal_str +=  "+"

    def restar(self):
        if self.__internal_str.find("-") == -1:
            self.__internal_str +=  "-"

    def p_izquierdo(self):
        if self.__internal_str.find("(") == -1:
            self.__internal_str +=  "("
      
    def p_derecho(self):
        if self.__internal_str.find(")") == -1:
            self.__internal_str +=  ")"
            
                        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())