from os import fsdecode
from stat import SF_APPEND
import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "semana_6/frmRegistroVentas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []

class FormularioVentas(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioVentas, self).__init__(parent)
        uic.loadUi("semana_6/frmRegistroVentas.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.show()

    # Aquí van los nuevos métodos
    def registrar(self):

        #Entrada de datos
        producto = self.cboProducto.currentText()
        tipoPago = self.cboPago.currentText()
        cantidad = int(self.txtCantidad.text())

        #Mostrar el precio del producto
        precio = 0
        if producto == "Colección Escolar": 
            precio = 240
        if producto == "Colección PreUniversitaria":
            precio = 150
        if producto == "Colección Profesional":
            precio = 350
        
        self.lblPrecio.setText("S/. " + str(precio))

        #Calculando el subtotal
        subtotal = precio * cantidad

        #Calculando el descuento y el recargo
        descuento = 0
        recargo = 0
        if tipoPago == "Contado":
            descuento = 0.05 * subtotal
        else:
            recargo = 0.10 * subtotal
        
        #Calculando el precio final
        precioFinal = subtotal - descuento + recargo

        #Agregando datos a la lista y mostrar datos en la tabla
        datos = (producto, str(cantidad), str(precio), tipoPago, str(descuento), str(recargo), str(precioFinal))
        lista.append(datos)
        self.listar()
    
    def listar(self):
        self.tblDatos.setRowCount(50)
        for i in range(0, len(lista)):
            self.tblDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4]))
            self.tblDatos.setItem(i, 5, QtWidgets.QTableWidgetItem(lista[i][5]))
            self.tblDatos.setItem(i, 6, QtWidgets.QTableWidgetItem(lista[i][6]))

    def nuevo(self):
        self.txtCantidad.clear()
        self.lblPrecio.clear()
        self.cboProducto.setCurrentIndex(0)
        self.cboPago.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioVentas()
    app.exec()
    
