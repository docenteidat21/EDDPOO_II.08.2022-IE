import sys
from PyQt5 import QtWidgets, uic
from claseRegistroAlumnos import RegistroAlumnos

qtCreatorFile = "SEMANA_10/PaqueteRegistroAlumnos/frmRegistroAlumnos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#Creación de objetos
alumno1 = RegistroAlumnos()

class FormularioRegistroAlumnos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioRegistroAlumnos, self).__init__(parent)
        uic.loadUi("SEMANA_10/PaqueteRegistroAlumnos/frmRegistroAlumnos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnMostrar.clicked.connect(self.mostrar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    def registrar(self):
        alumno1.setNombre(self.txtNombre.text())
        alumno1.setApellidoPaterno(self.txtApellidoPaterno.text())
        alumno1.setApellidoMaterno(self.txtApellidoMaterno.text())
        alumno1.setCodigo(self.txtCodigo.text())

        # Limpiamos las cajas de texto
        self.txtNombre.setText("")
        self.txtApellidoPaterno.setText("")
        self.txtApellidoMaterno.setText("")
        self.txtCodigo.setText("")

    def imprimir(self, cad):
        self.txtS.append(cad)
    
    def mostrar(self):
        self.txtS.setText("")
        self.imprimir("NOMBRE\t: " + alumno1.getNombre())
        self.imprimir("APELLIDO PATERNO\t: " + alumno1.getApellidoPaterno())
        self.imprimir("APELLIDO MATERNO\t: " + alumno1.getApellidoMaterno)
        self.imprimir("CODIGO\t: " + alumno1.getCodigo())
        self.imprimir("")

    def limpiar(self):
        # limpiamos las cajas de texto y el área de texto
        self.txtNombre.setText("")
        self.txtApellidoPaterno.setText("")
        self.txtApellidoMaterno.setText("")
        self.txtCodigo.setText("")
        self.txtS.setText("")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window =  FormularioRegistroAlumnos()
    app.exec()