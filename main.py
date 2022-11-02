import sys
from PySide2.QtWidgets import QMainWindow, QApplication

from py_windows.window_form_alumno import FormAlumnoWindow
from py_windows.window_form_grupo import FormGrupoWindow
from py_windows.window_table_alumno import TableAlumnoWindow
from ui_windows.ui_menu_alumno import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lista_alumnos = []
        self.lista_grupos = []

        self.form_alumno_window = FormAlumnoWindow(self.lista_alumnos)
        self.form_grupo_window = FormGrupoWindow(self.lista_grupos)
        self.table_alumno_window = TableAlumnoWindow(self.lista_alumnos, self.lista_grupos)

    def show_new_student_window(self):
        self.form_alumno_window.show()

    def show_create_group_window(self):
        self.form_grupo_window.show()

    def show_student_list_window(self):
        self.table_alumno_window.show()

    def perform_exit(self):
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
