from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_form_grupo import Ui_MainWindow
from utils.grupo import Grupo


class FormGrupoWindow(QMainWindow):
    def __init__(self, grupos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.grupos = grupos

    def clear_button(self):
        self.ui.le_nombre.clear()
        self.ui.le_descripcion.clear()

    def send_button(self):
        nombre = self.ui.le_nombre.text()
        descripcion = self.ui.le_descripcion.text()
        self.grupos.append(Grupo(nombre, descripcion))
        print(self.grupos)

