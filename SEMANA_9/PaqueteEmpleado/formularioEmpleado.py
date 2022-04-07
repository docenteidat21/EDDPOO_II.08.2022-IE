import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado

qtCreatorFile = "SEMANA_9/PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioEmpleado, self).__init__(parent)
        uic.loadUi("SEMANA_9/PaqueteEmpleado/frmEmpleado.ui", self)

        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    def procesar(self):
        empleado1 = Empleado(1234, "Kenny", 20, 45.5)
        self.mostrarDatos(empleado1)

        empleado2 = Empleado(2345, "Jesús", 30, 42.5)
        self.mostrarDatos(empleado2)

    def imprimir(self, cad):
        self.txtS.append(cad)
    
    def mostrarDatos(self, Empleado):
        self.imprimir("CÓDIGO\t: " + str(Empleado.getCodigo()))
        self.imprimir("NOMBRE\t: " + str(Empleado.getNombre()))
        self.imprimir("HORAS\t: " + str(Empleado.getHoras()))
        self.imprimir("TARIFA\t: " + str(Empleado.getTarifa()))
        self.imprimir("")
        self.imprimir("SUELDO BRUTO\t: " + str(Empleado.sueldoBruto()))
        self.imprimir("DESCUENTO\t: " + str(Empleado.descuento()))
        self.imprimir("SUELDO NETO\t: " + str(Empleado.sueldoNeto()))
        self.imprimir("")

    def limpiar(self):
        self.txtS.setText("")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioEmpleado()
    app.exec()