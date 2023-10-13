from Ui_dialogo import *
from Ui_menu import *
from PyQt6.QtWidgets import QMainWindow
import sys
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *aparent, **flags):
        super().__init__(*aparent, **flags)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()    
    window.show()
    sys.exit(app.exec())
        