from PySide2.QtGui import QBrush, QColor
from PySide2.QtWidgets import QTableWidgetItem


class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.dni = self.fix_dni(dni)
        self.grupo = None
        self.color = None

    def fix_dni(self, dni):
        fixed_dni = ["0"]*8
        dni = dni.replace(".", "")
        for i, element in enumerate(dni):
            fixed_dni[i] = element
        return "".join(fixed_dni)

    def new_item_with_background(self, text):
        item = QTableWidgetItem(str(text))
        if self.color:
            item.setBackground(QBrush(QColor(self.color)))
        return item

    def convertir_a_qt(self):
        return [
            (0, self.new_item_with_background(self.show_dni())),
            (1, self.new_item_with_background(self.nombre)),
            (2, self.new_item_with_background(self.apellido)),
            (3, self.new_item_with_background(repr(self.grupo))),
        ]

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"

    def __repr__(self):
        return str(self.dni)

    def starts_with_dni(self, dni):
        for i in range(len(dni)):
            if dni[i] != self.dni[i]:
                return False
        return True

    def exact_match_dni(self, dni):
        return self.dni == dni

    def copy_with_color(self, color):
        copy = self.__copy__()
        copy.grupo = self.grupo
        copy.color = color
        return copy

    def __copy__(self):
        return Alumno(self.nombre, self.apellido, self.dni)

    def show_dni(self):
        return f"{self.dni[:2]}.{self.dni[2:5]}.{self.dni[5:]}"
