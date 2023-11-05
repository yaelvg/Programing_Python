from PyQt6 import QtCore,QtGui,QtWidgets
from Ui_Simon import *
from Ui_PrincipalSimon import *
from Ui_Instrucciones import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QWidget, QApplication
import sys
import pyfirmata

class Principal(QMainWindow, Ui_PrincipalSimon):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        self.ventana=MainWindow()
        self.instruc=Instrucciones()

        

        self.pushButton.clicked.connect(self.jugar)
        self.pushButton_2.clicked.connect(self.instrucciones)
        
    def jugar(self):
        self.ventana.show()
        self.close()
    
    def instrucciones(self):
        self.instruc.show()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        # *Seccion de botones
        self.Rojobtn.clicked.connect(self.rojo)
        self.Amarillobtn.clicked.connect(self.amarillo)
        self.Azulbtn.clicked.connect(self.azul)
        self.Verdebtn.clicked.connect(self.verde)
        self.Apagarbtn.clicked.connect(self.apagado)
        self.perderbtn.clicked.connect(self.mensage)

    def rojo(self):
        for Qlabel in window.findChildren(QWidget):
            if Qlabel is not self.Rojo:
                Qlabel.lower()
        self.Rojo.raise_()

    def amarillo(self):
        for Qlabel in window.findChildren(QWidget):
            if Qlabel is not self.Amarillo:
                Qlabel.lower()
        self.Amarillo.raise_()
    
    def azul(self):
        for Qlabel in window.findChildren(QWidget):
            if Qlabel is not self.Azul:
                Qlabel.lower()
        self.Azul.raise_()

    def verde(self):
        for Qlabel in window.findChildren(QWidget):
            if Qlabel is not self.Verde:
                Qlabel.lower()
        self.Verde.raise_()
    
    def apagado(self):
        for Qlabel in window.findChildren(QWidget):
            if Qlabel is not self.Apagada:
                Qlabel.lower()
        self.Apagada.raise_()
    
    def mensage(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Mensaje")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Perdiste")
        msg.setInformativeText(f"Lo siento.Perdiste")
        #msg.setDetailedText("Saluditos")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        res = msg.exec()
        print(res)

class Instrucciones(QMainWindow, Ui_Dialog):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec())