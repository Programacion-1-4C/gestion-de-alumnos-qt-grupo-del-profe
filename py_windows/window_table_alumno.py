from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_table_alumno import Ui_MainWindow


class TableAlumnoWindow(QMainWindow):
    def __init__(self, ref_list_alumnos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ref_list_alumnos = ref_list_alumnos

    def showEvent(self, event):
        super().showEvent(event)
        print(self.ref_list_alumnos)
        self.ui.tw_alumnos.setRowCount(len(self.ref_list_alumnos))
        for i, element in enumerate(self.ref_list_alumnos):
            for j in element.convertir_a_qt():
                self.ui.tw_alumnos.setItem(i, *j)
