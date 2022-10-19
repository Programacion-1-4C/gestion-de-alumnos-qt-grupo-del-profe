from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_table_alumno import Ui_MainWindow


class TableAlumnoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

