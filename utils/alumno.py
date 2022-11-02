from PySide2.QtWidgets import QWidgetItem


class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def convertir_a_qt(self):
        return [
            (1, QWidgetItem(str(self.nombre))),
            (2, QWidgetItem(str(self.apellido))),
            (3, QWidgetItem(str(self.dni)))
        ]