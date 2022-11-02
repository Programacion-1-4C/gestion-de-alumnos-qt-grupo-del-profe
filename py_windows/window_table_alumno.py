from PySide2.QtWidgets import QMainWindow

from ui_windows.ui_table_alumno import Ui_MainWindow


class TableAlumnoWindow(QMainWindow):
    def __init__(self, ref_list_alumnos, ref_list_grupos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ref_list_alumnos = ref_list_alumnos
        self.ref_list_grupos = ref_list_grupos

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


    def search_button(self):
        pass

    def clear_button(self):
        pass

    def assign_button(self):
        grupo = self.ref_list_grupos[self.ui.cb_grupos.currentIndex()]
        seleccionados = set()
        for seleccionado in self.ui.tw_alumnos.selectedIndexes():
            seleccionados.add(seleccionado.row())
        for i in seleccionados:
            self.ref_list_alumnos[i].grupo = grupo

        self.redraw()

