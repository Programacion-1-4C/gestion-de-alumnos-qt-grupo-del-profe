from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_form_alumno import Ui_MainWindow
from utils.alumno import Alumno


class FormAlumnoWindow(QMainWindow):
    def __init__(self, ref_lista_alumnos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ref_lista_alumnos = ref_lista_alumnos

    def clean_button(self):
        self.ui.le_nombre.setText("")
        self.ui.le_apellido.setText("")
        self.ui.le_dni.setText("")

    def send_button(self):
        nombre = self.ui.le_nombre.text()
        apellido = self.ui.le_apellido.text()
        dni = self.ui.le_dni.text()
        alumno = Alumno(nombre, apellido, dni)
        self.ref_lista_alumnos.append(alumno)

