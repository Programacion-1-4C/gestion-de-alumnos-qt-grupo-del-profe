# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_alumnoMDkIhC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 168)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_ingresar_alumno = QPushButton(self.centralwidget)
        self.pb_ingresar_alumno.setObjectName(u"pb_ingresar_alumno")

        self.verticalLayout.addWidget(self.pb_ingresar_alumno)

        self.pb_crear_grupo = QPushButton(self.centralwidget)
        self.pb_crear_grupo.setObjectName(u"pb_crear_grupo")

        self.verticalLayout.addWidget(self.pb_crear_grupo)

        self.pb_lista_alumnos = QPushButton(self.centralwidget)
        self.pb_lista_alumnos.setObjectName(u"pb_lista_alumnos")

        self.verticalLayout.addWidget(self.pb_lista_alumnos)

        self.pb_salir = QPushButton(self.centralwidget)
        self.pb_salir.setObjectName(u"pb_salir")

        self.verticalLayout.addWidget(self.pb_salir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_ingresar_alumno.clicked.connect(MainWindow.show_new_student_window)
        self.pb_crear_grupo.clicked.connect(MainWindow.show_create_group_window)
        self.pb_lista_alumnos.clicked.connect(MainWindow.show_student_list_window)
        self.pb_salir.clicked.connect(MainWindow.perform_exit)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pb_ingresar_alumno.setText(QCoreApplication.translate("MainWindow", u"Ingresar Alumno", None))
        self.pb_crear_grupo.setText(QCoreApplication.translate("MainWindow", u"Crear Grupo", None))
        self.pb_lista_alumnos.setText(QCoreApplication.translate("MainWindow", u"Lista Alumnos", None))
        self.pb_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

