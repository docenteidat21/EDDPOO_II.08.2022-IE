import sys
from PyQt5 import QtWidgets, uic
from claseAlumno import Alumno

qtCreatorFile = "SEMANA_9/PaqueteAlumno2/frmAlumno.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioAlumno(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioAlumno, self).__init__(parent)
        uic.loadUi("SEMANA_9/PaqueteAlumno2/frmAlumno.ui", self)

        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    def procesar(self):
        alumno1 = Alumno("Vanessa", 20, 15)
        self.mostrarDatos(alumno1)

        alumno2 = Alumno("Valentina", 20, 19)
        self.mostrarDatos(alumno2)

        alumno3 = Alumno("Cecilia", 10, 12)
        self.mostrarDatos(alumno3)

    def imprimir(self, cad):
        self.txtS.append(cad)
    
    def mostrarDatos(self, Alumno):
        self.imprimir("NOMBRE\t: " + str(Alumno.getNombre()))
        self.imprimir("NOTA 1\t: " + str(Alumno.getNota1()))
        self.imprimir("NOTA 2\t: " + str(Alumno.getNota2))
        self.imprimir("PROMEDIO\t: " + str(Alumno.promedio()))
        self.imprimir("")

    def limpiar(self):
        self.txtS.setText("")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioAlumno()
    app.exec()