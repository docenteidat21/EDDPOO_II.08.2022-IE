import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "semana_5/frmAreaTriangulo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AreaTriangulo(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(AreaTriangulo, self).__init__(parent)
        uic.loadUi("semana_5/frmAreaTriangulo.ui", self)

        # Aquí van los botones
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    #Aquí van las funciones o métodos

    def calcular(self):
        
        # Entrada de datos
        base = float(self.txtBase.text())
        altura = float(self.txtAltura.text())

        # Proceso de cálculo
        area = (base * altura) / 2

        # Salida de resultados
        self.txtS.setText("ÁREA DEL TRIÁNGULO:\n")
        self.txtS.append("El valor de la base es: " + str(base))
        self.txtS.append("El valor de la altura es: " + str(altura))
        self.txtS.append("El valor del área es: " + str(area))

    def limpiar(self):
        self.txtBase.setText("")
        self.txtAltura.setText("")
        self.txtS.setText("")

    def salir(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AreaTriangulo()
    app.exec() 