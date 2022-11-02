# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_grupogcoHsC.ui'
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
        MainWindow.resize(295, 139)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_nombre = QLineEdit(self.centralwidget)
        self.le_nombre.setObjectName(u"le_nombre")
        self.le_nombre.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nombre)

        self.le_descripcion = QLineEdit(self.centralwidget)
        self.le_descripcion.setObjectName(u"le_descripcion")
        self.le_descripcion.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_descripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_limpiar = QPushButton(self.centralwidget)
        self.pb_limpiar.setObjectName(u"pb_limpiar")

        self.horizontalLayout.addWidget(self.pb_limpiar)

        self.pb_enviar = QPushButton(self.centralwidget)
        self.pb_enviar.setObjectName(u"pb_enviar")

        self.horizontalLayout.addWidget(self.pb_enviar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_limpiar.clicked.connect(MainWindow.clear_button)
        self.pb_enviar.clicked.connect(MainWindow.send_button)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Formulario Grupo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.pb_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pb_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

