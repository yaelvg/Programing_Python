# Form implementation generated from reading ui file 'c:\Users\sergi\OneDrive\Documentos\UPIITA\4 Semestre\Programacion Avanzada\Practica6\Simon.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\logo.jpeg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Apagada = QtWidgets.QLabel(parent=self.centralwidget)
        self.Apagada.setEnabled(True)
        self.Apagada.setGeometry(QtCore.QRect(160, 60, 511, 441))
        self.Apagada.setStyleSheet("border-image: url(:/simon/OneDrive/Documentos/UPIITA/4 Semestre/Programacion Avanzada/Practica6/SIMONtodasapagadas.png);")
        self.Apagada.setText("")
        self.Apagada.setPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\SIMONtodasapagadas.png"))
        self.Apagada.setScaledContents(True)
        self.Apagada.setObjectName("Apagada")
        self.Rojobtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Rojobtn.setGeometry(QtCore.QRect(490, 520, 75, 24))
        self.Rojobtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Rojobtn.setText("")
        self.Rojobtn.setObjectName("Rojobtn")
        self.Amarillo = QtWidgets.QLabel(parent=self.centralwidget)
        self.Amarillo.setEnabled(True)
        self.Amarillo.setGeometry(QtCore.QRect(160, 60, 511, 441))
        self.Amarillo.setStyleSheet("border-image: url(:/simon/OneDrive/Documentos/UPIITA/4 Semestre/Programacion Avanzada/Practica6/simonAmarilloP.png);")
        self.Amarillo.setText("")
        self.Amarillo.setPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\simonAmarilloP.png"))
        self.Amarillo.setScaledContents(True)
        self.Amarillo.setObjectName("Amarillo")
        self.Verdebtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Verdebtn.setGeometry(QtCore.QRect(570, 520, 75, 24))
        self.Verdebtn.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.Verdebtn.setText("")
        self.Verdebtn.setObjectName("Verdebtn")
        self.Azulbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Azulbtn.setGeometry(QtCore.QRect(650, 520, 75, 24))
        self.Azulbtn.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.Azulbtn.setText("")
        self.Azulbtn.setObjectName("Azulbtn")
        self.Rojo = QtWidgets.QLabel(parent=self.centralwidget)
        self.Rojo.setGeometry(QtCore.QRect(160, 60, 511, 441))
        self.Rojo.setStyleSheet("border-image: url(:/simon/OneDrive/Documentos/UPIITA/4 Semestre/Programacion Avanzada/Practica6/simonsinfondo.png);")
        self.Rojo.setText("")
        self.Rojo.setPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\simonRojoP.png"))
        self.Rojo.setScaledContents(True)
        self.Rojo.setObjectName("Rojo")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 20, 118, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Azul = QtWidgets.QLabel(parent=self.centralwidget)
        self.Azul.setGeometry(QtCore.QRect(160, 60, 511, 441))
        self.Azul.setStyleSheet("border-image: url(:/simon/OneDrive/Documentos/UPIITA/4 Semestre/Programacion Avanzada/Practica6/simonAzulP.png);")
        self.Azul.setText("")
        self.Azul.setPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\simonAzulP.png"))
        self.Azul.setScaledContents(True)
        self.Azul.setObjectName("Azul")
        self.Verde = QtWidgets.QLabel(parent=self.centralwidget)
        self.Verde.setGeometry(QtCore.QRect(160, 60, 511, 441))
        self.Verde.setStyleSheet("border-image: url(:/simon/OneDrive/Documentos/UPIITA/4 Semestre/Programacion Avanzada/Practica6/simonverdeP.png);")
        self.Verde.setText("")
        self.Verde.setPixmap(QtGui.QPixmap("c:\\Users\\sergi\\OneDrive\\Documentos\\UPIITA\\4 Semestre\\Programacion Avanzada\\Practica6\\simonverdeP.png"))
        self.Verde.setScaledContents(True)
        self.Verde.setObjectName("Verde")
        self.Amarillobtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Amarillobtn.setGeometry(QtCore.QRect(730, 520, 75, 24))
        self.Amarillobtn.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Amarillobtn.setText("")
        self.Amarillobtn.setObjectName("Amarillobtn")
        self.Apagarbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Apagarbtn.setGeometry(QtCore.QRect(30, 480, 75, 24))
        self.Apagarbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Apagarbtn.setText("")
        self.Apagarbtn.setObjectName("Apagarbtn")
        self.perderbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.perderbtn.setGeometry(QtCore.QRect(30, 440, 75, 24))
        self.perderbtn.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.perderbtn.setText("")
        self.perderbtn.setObjectName("perderbtn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 10, 121, 41))
        self.label.setStyleSheet("font: 700 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.iniciobtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.iniciobtn.setGeometry(QtCore.QRect(40, 320, 91, 41))
        self.iniciobtn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 15px;")
        self.iniciobtn.setObjectName("iniciobtn")
        self.Rojobtn.raise_()
        self.Verdebtn.raise_()
        self.Azulbtn.raise_()
        self.progressBar.raise_()
        self.Azul.raise_()
        self.Verde.raise_()
        self.Amarillobtn.raise_()
        self.Amarillo.raise_()
        self.Rojo.raise_()
        self.Apagada.raise_()
        self.Apagarbtn.raise_()
        self.perderbtn.raise_()
        self.label.raise_()
        self.iniciobtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simon Dice"))
        self.label.setText(_translate("MainWindow", "SCORE :"))
        self.iniciobtn.setText(_translate("MainWindow", "INICIAR"))