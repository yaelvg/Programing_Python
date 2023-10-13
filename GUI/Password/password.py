from Ui_Password import *
from PyQt6.QtWidgets import QMainWindow, QDialog
import sys
from PyQt6.uic import loadUi #Duda de clase no se bien como funciona

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
    #'No se a que se refirere los parametrso parent y flags'
        super().__init__(*parent, **flags)
        self.setupUi(self)
        #coneccion del botton
        self.pushButton.clicked.connect(self.showDialog)
    
    def showDialog(self):
        dialog = MiDialog(self)
        resp=dialog.exec()
        if resp == 1:
            user= dialog.edit_usuario.text()
            password=dialog.edit_Password.text()
            if user == "Alejandro" and password == "xxx":
                self.label.setText("Bienvenido Alejanfro")
            else:
                self.label.setText("Hola desconocido")
        else:
            self.label.setText("Hola desconocido")
        


class MiDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Password.ui',self)
        
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
        