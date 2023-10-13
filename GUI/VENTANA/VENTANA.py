from Ui_VENTANA_1 import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        #Conecta el boton
        self.pushButton_2.clicked.connect(self.showMessage)
        
    def showMessage(self):
        QMessageBox.information(self, 'Message', f'Hola {self.lineEdit.text()}')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()    
    window.show()
    sys.exit(app.exec())
        
