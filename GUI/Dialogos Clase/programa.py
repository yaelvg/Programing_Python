from Ui_dialogo import *
from Ui_menu import *
from PyQt6.QtWidgets import QMainWindow, QDialog
import sys
'''Etiqueta para importar el dialogo'''
from PyQt6.uic import loadUi

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *aparent, **flags):
        super().__init__(*aparent, **flags)
        self.setupUi(self)
    
    def MostrarDialog(self):
        dialogo= Dialogo()
        dialogo.exec()
        
        
class   Dialogo(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        loadUi("dialogo.ui".self)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()    
    window.show()
    sys.exit(app.exec())
        