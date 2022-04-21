from PyQt5 import QtWidgets, uic
from Vista.VentanaPrincipal import VentanaPrincipal
#from Controlador.arregloProductos import *
#from Controlador.arregloClientes import *
#from Controlador.arregloDetalleVenta import *
#from Controlador.arregloFactura import *

qtCreatorFile = "PROYECTO/UI/login.ui" # Nombre del archivo aquí!!!
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        uic.loadUi("PROYECTO/UI/login.ui",self)
             
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()
        if usuario == "kenny" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()         
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos ingresados son incorrectos...!!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            #QtWidgets.QMessageBox.information(self, "Registrar Producto", "El código ingesado ya existe...!!!", QtWidgets.QMessageBox.Ok)
            x = mensaje.exec_()
            self.txtUsuario.setText("")
            self.txtPassword.setText("")