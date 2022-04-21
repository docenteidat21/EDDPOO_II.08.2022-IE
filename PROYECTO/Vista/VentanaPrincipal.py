from PyQt5 import QtWidgets, uic
from Controlador.ArrregloProductos import *
from Controlador.ArregloClientes import *
from Controlador.ArregloDetalleVenta import *
from Controlador.ArregloFactura import *
from Vista.VentanaClientes import *
from Vista.VentanaDetalleVenta import *
from Vista.VentanaFactura import *
from Vista.VentanaProductos import *
from Vista.VentanaVentas import *

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        uic.loadUi("PROYECTO/UI/ventanaPrincipal.ui",self)
        
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnVender.clicked.connect(self.abrirVentanaVentas)
        self.btnDetalleVentas.clicked.connect(self.abrirVentanaDetalleVentas)
        self.btnVentas.clicked.connect(self.abrirVentanaFacturas)
        self.btnSalir.clicked.connect(self.cerrar)
        
    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def abrirVentanaVentas(self):
        vVentas = VentanaVentas(self)
        vVentas.show()
    
    def abrirVentanaDetalleVentas(self):
        vDetalleVentas = VentanaDetalleVentas(self)
        vDetalleVentas.show()
    
    def abrirVentanaFacturas(self):
        vFacturas = VentanaFacturas(self)
        vFacturas.show()

    def cerrar(self):
        self.close()