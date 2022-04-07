import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "semana_4/formularioPrueba.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("semana_4/evaluacion_continua1/formularioPrueba.ui", self)

        # Aquí van las funciones
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    def procesar(self):
        self.lblTexto.setText("Mi nombre es Kenny")
    
    def limpiar(self):
        self.lblTexto.setText("Pulsa nuevamente en el botón Procesar...!!!")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec() 



