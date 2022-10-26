# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_alumnothTjmN.ui'
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
        MainWindow.resize(422, 304)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_alumnos = QTableWidget(self.centralwidget)
        if (self.tw_alumnos.columnCount() < 4):
            self.tw_alumnos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_alumnos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_alumnos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_alumnos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_alumnos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_alumnos.setObjectName(u"tw_alumnos")

        self.verticalLayout.addWidget(self.tw_alumnos)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_dni = QLineEdit(self.centralwidget)
        self.le_dni.setObjectName(u"le_dni")
        self.le_dni.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_dni)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_borrar = QPushButton(self.centralwidget)
        self.pb_borrar.setObjectName(u"pb_borrar")

        self.horizontalLayout.addWidget(self.pb_borrar)

        self.pb_buscar = QPushButton(self.centralwidget)
        self.pb_buscar.setObjectName(u"pb_buscar")

        self.horizontalLayout.addWidget(self.pb_buscar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tw_alumnos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"DNI", None));
        ___qtablewidgetitem1 = self.tw_alumnos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tw_alumnos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem3 = self.tw_alumnos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Grupo", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.le_dni.setInputMask(QCoreApplication.translate("MainWindow", u"99.999.999", None))
        self.pb_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.pb_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
    # retranslateUi

