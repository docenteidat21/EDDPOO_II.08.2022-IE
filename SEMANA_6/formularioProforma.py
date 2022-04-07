import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "semana_6/frmProforma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Proforma(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Proforma, self).__init__(parent)
        uic.loadUi("semana_6/frmProforma.ui", self)

        self.btnCalcular.clicked.connect(self.calcular)
        self.show()
    
    # Aquí van las nuevas funciones

    def calcular(self):

        # Entrada de datos
        precio = float(self.txtPrecio.text())
        cantidad = int(self.spbCantidad.value())

        # Calculamos el importe
        importe = precio * cantidad

        # Calculamos el descuento
        porcentajeDescuento = 0
        if self.rbMayorista.isChecked() == True:
            porcentajeDescuento = 4.5/100
        if self.rbMinorista.isChecked() == True:
            porcentajeDescuento = 1.9 / 100
        
        descuento = importe * porcentajeDescuento

        # Calculamos el interés
        porcentajeInteres = 0
        if self.rbInteres1.isChecked() == True:
            porcentajeInteres = 0/100
        if self.rbInteres2.isChecked() == True:
            porcentajeInteres = 8.5/100
        if self.rbInteres3.isChecked() == True:
            porcentajeInteres = 12.5/100
        
        interes = importe * porcentajeInteres

        # Calculamos el total
        total = importe - descuento + interes

        # Salida de resultados
        self.txtImporte.setText("S/. " + str(importe))
        self.txtDescuentos.setText("S/. " + str(descuento))
        self.txtInteres.setText("S/. " + str(interes))
        self.txtTotal.setText("S/. " + str(total))

        self.txtS.setText("========================")
        self.txtS.append("PROFORMA")
        self.txtS.append("========================")
        self.txts.append("CÓDIGO DEL CLIENTE: " + self.txtCodigoCliente.text())
        self.txtS.append("NOMBRE DEL CLIENTE: " + self.txtNombreCliente.text())
                


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Proforma()
    app.exec()
    




