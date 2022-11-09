from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_table_alumno import Ui_MainWindow


class TableAlumnoWindow(QMainWindow):
    def __init__(self, ref_list_alumnos, ref_list_grupos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ref_list_alumnos = ref_list_alumnos
        self.ref_list_grupos = ref_list_grupos

        self.backup_list = None

    def redraw(self):
        self.ui.tw_alumnos.setRowCount(len(self.ref_list_alumnos))
        for i, element in enumerate(self.ref_list_alumnos):
            for j in element.convertir_a_qt():
                self.ui.tw_alumnos.setItem(i, *j)

    def showEvent(self, event):
        super().showEvent(event)
        self.redraw()

        self.ui.cb_grupos.clear()
        self.ui.cb_grupos.addItems([x.nombre for x in self.ref_list_grupos])


    def filter_students(self, dni):
        exact_match = []
        filtered = []
        for alumno in self.ref_list_alumnos:
            if alumno.exact_match_dni(dni):
                exact_match.append(alumno)
            elif alumno.starts_with_dni(dni):
                filtered.append(alumno)
        self.ref_list_alumnos = [*exact_match, *filtered]


    def filter_students_color(self, dni):
        exact_match = []
        filtered = []
        not_match = []
        for alumno in self.ref_list_alumnos:
            if alumno.exact_match_dni(dni):
                exact_match.append(alumno.copy_with_color("Green"))
            elif alumno.starts_with_dni(dni):
                filtered.append(alumno.copy_with_color("Yellow"))
            else:
                not_match.append(alumno.copy_with_color("Red"))
        self.ref_list_alumnos = [*exact_match, *filtered, *not_match]


    def search_button(self):
        self.deback_up_list()
        self.backup_list = [*self.ref_list_alumnos]
        dni = self.ui.le_dni.text().replace(".", "")
        self.filter_students_color(dni)
        self.redraw()


    def deback_up_list(self):
        if self.backup_list:
            self.ref_list_alumnos = self.backup_list
            self.backup_list = None

    def clear_button(self):
        self.deback_up_list()
        self.redraw()

    def assign_button(self):
        grupo = self.ref_list_grupos[self.ui.cb_grupos.currentIndex()]
        seleccionados = set()
        for seleccionado in self.ui.tw_alumnos.selectedIndexes():
            seleccionados.add(seleccionado.row())
        for i in seleccionados:
            self.ref_list_alumnos[i].grupo = grupo

        self.redraw()

