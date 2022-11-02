from PySide2.QtWidgets import QTableWidgetItem


class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.dni = dni
        self.grupo = None

    def convertir_a_qt(self):
        return [
            (0, QTableWidgetItem(str(self.dni))),
            (1, QTableWidgetItem(str(self.nombre))),
            (2, QTableWidgetItem(str(self.apellido))),
            (3, QTableWidgetItem(repr(self.grupo))),
        ]

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"

    def __repr__(self):
        return str(self.dni)
