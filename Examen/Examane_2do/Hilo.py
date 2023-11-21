from PyQt6.QtCore import QThread, pyqtSignal
import random as rand
import pyfirmata
import inspect
import time

class Hilo(QThread):
    
    def __init__(self, main_window_instance):
        super().__init__()
        self.main_window = main_window_instance
        
    # signal_azul = pyqtSignal()
    # signal_rojo = pyqtSignal()
    # signal_verde = pyqtSignal()
    # signal_amarillo = pyqtSignal()
    # signal_apagado=pyqtSignal()
        
    
    def signals(self, x):
        """Emecion de signal desde la clase JuegoSimon

        Args:
            x (int): Pin correspondiente a la conexion fisica de leds

        Returns:
            signal: returna una emicion de la signal correspondiente a cada pin
        """
        if x == 2:
            return self.signal_azul.emit()
        
        elif x == 3:
            return self.signal_rojo.emit()
        
        elif x == 4: 
            return self.signal_verde.emit()
        
        elif x == 5:
            return self.signal_amarillo.emit()
        
        elif x == 6:
            return self.signal_apagado.emit()
        
        
    final_programa = pyqtSignal()  # * Señal que indica el final del juego
    
    
    def run(self):
        
        if not hasattr(inspect, 'getargspec'):
            inspect.getargspec = inspect.getfullargspec

        '''inicio del puerto y comunicacion'''
        board = pyfirmata.Arduino('COM5')
        it = pyfirmata.util.Iterator(board)
        it.start()

        
        azul = board.get_pin('d:2:o')
        rojo = board.get_pin('d:3:o')
        verde = board.get_pin('d:4:o')
        amarillo= board.get_pin('d:5:o')
        blanco = board.get_pin('d:6:o')
                
                
        '''Variables de ayuda'''
        boton =1
        boton_salir = 0
        def ruleta():
            
            while True:
                for i in range(2,7):
                    board.digital[i].write(1)
                    time.sleep(1/10)
                    board.digital[i].write(0)
                
            for i in range(6,1):
                board.digital[i].write(1)
                time.sleep(1/10)
                board.digital[i].write(0)
                

        def inicio():
            """Secuencia de inicio
            """
            for i in range(2,7):
                board.digital[i].write(1)
                time.sleep(1/10)
                board.digital[i].write(0)
                
            for i in range(6,1):
                board.digital[i].write(1)
                time.sleep(1/10)
                board.digital[i].write(0)


            '''Principal -Loop-'''
        inicio()
        while True:
            
            boton=0
            boton_salir= 0
            
            ruleta()
            
            if boton == 1:
                boton=0
                for i in range(2,7):
                    board.digital[i].write(0)
                    
                x=rand.randint(2,7)
                board.digital[i].write(x)
                
                if boton == 1:
                    break
                
            if boton_salir== 1:
                self.final_programa.emit()