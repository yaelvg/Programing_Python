from Ui_botones import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        #Conecta el boton
        '''De primera instancia podemos desactivar ciertos elementos de la GUI
        '''
        self.boton_desactivar.setEnabled(False)
        '''Obtenemos el click del boton acti'''
        self.boton_activar.clicked.connect(self.showMessage)
        #self.pushButton.clicked.connect(self.showMessage)
        
    def showMessage(self):
        #self.boton_activar.clicked.connect(False)
        self.boton_desactivar.clicked.connect(True)
        self.etiqueta.setText("ACTIVADO")
    # QMessageBox.information(self, 'Message', f'Hola {self.lineEdit.text()}')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()    
    window.show()
    sys.exit(app.exec())