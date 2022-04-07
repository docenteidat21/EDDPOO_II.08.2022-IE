from PyQt5 import QtWidgets, uic
from Vista.VentanaProductos import *

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("PROYECTO/UI/VentanaPrincipal.ui", self)

        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
    
    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()



