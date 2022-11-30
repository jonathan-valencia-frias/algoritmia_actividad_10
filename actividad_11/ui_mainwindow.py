# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formularioparticulasbGzXRV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 619)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tab_all = QTabWidget(self.centralwidget)
        self.tab_all.setObjectName(u"tab_all")
        self.tab_all.setGeometry(QRect(0, 0, 581, 551))
        self.agregar = QWidget()
        self.agregar.setObjectName(u"agregar")
        self.mostrar_datos = QPushButton(self.agregar)
        self.mostrar_datos.setObjectName(u"mostrar_datos")
        self.mostrar_datos.setGeometry(QRect(80, 320, 161, 41))
        self.Canvas_mostrar = QPlainTextEdit(self.agregar)
        self.Canvas_mostrar.setObjectName(u"Canvas_mostrar")
        self.Canvas_mostrar.setGeometry(QRect(330, 0, 191, 481))
        self.layoutWidget = QWidget(self.agregar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 3, 321, 311))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.text_id = QLabel(self.layoutWidget)
        self.text_id.setObjectName(u"text_id")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.text_id)

        self.input_id = QLineEdit(self.layoutWidget)
        self.input_id.setObjectName(u"input_id")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_id)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.input_origenx = QLineEdit(self.layoutWidget)
        self.input_origenx.setObjectName(u"input_origenx")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.input_origenx)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.input_origeny = QLineEdit(self.layoutWidget)
        self.input_origeny.setObjectName(u"input_origeny")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.input_origeny)

        self.text_destinox = QLabel(self.layoutWidget)
        self.text_destinox.setObjectName(u"text_destinox")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.text_destinox)

        self.input_destinox = QLineEdit(self.layoutWidget)
        self.input_destinox.setObjectName(u"input_destinox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.input_destinox)

        self.text_destinoy = QLabel(self.layoutWidget)
        self.text_destinoy.setObjectName(u"text_destinoy")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.text_destinoy)

        self.input_destinoy = QLineEdit(self.layoutWidget)
        self.input_destinoy.setObjectName(u"input_destinoy")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.input_destinoy)

        self.text_velocidad = QLabel(self.layoutWidget)
        self.text_velocidad.setObjectName(u"text_velocidad")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.text_velocidad)

        self.input_velocidad = QLineEdit(self.layoutWidget)
        self.input_velocidad.setObjectName(u"input_velocidad")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.input_velocidad)

        self.text_red = QLabel(self.layoutWidget)
        self.text_red.setObjectName(u"text_red")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.text_red)

        self.input_red = QLineEdit(self.layoutWidget)
        self.input_red.setObjectName(u"input_red")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.input_red)

        self.text_green = QLabel(self.layoutWidget)
        self.text_green.setObjectName(u"text_green")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.text_green)

        self.input_green = QLineEdit(self.layoutWidget)
        self.input_green.setObjectName(u"input_green")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.input_green)

        self.text_blue = QLabel(self.layoutWidget)
        self.text_blue.setObjectName(u"text_blue")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.text_blue)

        self.input_blue = QLineEdit(self.layoutWidget)
        self.input_blue.setObjectName(u"input_blue")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.input_blue)

        self.btn_enviar_final = QPushButton(self.layoutWidget)
        self.btn_enviar_final.setObjectName(u"btn_enviar_final")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.btn_enviar_final)

        self.btn_inicio = QPushButton(self.layoutWidget)
        self.btn_inicio.setObjectName(u"btn_inicio")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.btn_inicio)

        self.tab_all.addTab(self.agregar, "")
        self.Tabla = QWidget()
        self.Tabla.setObjectName(u"Tabla")
        self.gridLayout = QGridLayout(self.Tabla)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buscar_button = QPushButton(self.Tabla)
        self.buscar_button.setObjectName(u"buscar_button")

        self.gridLayout.addWidget(self.buscar_button, 1, 1, 1, 1)

        self.buscar_text = QLineEdit(self.Tabla)
        self.buscar_text.setObjectName(u"buscar_text")

        self.gridLayout.addWidget(self.buscar_text, 1, 0, 1, 1)

        self.Btn_ordenarid = QPushButton(self.Tabla)
        self.Btn_ordenarid.setObjectName(u"Btn_ordenarid")

        self.gridLayout.addWidget(self.Btn_ordenarid, 2, 0, 1, 1)

        self.Btn_ordenarvel = QPushButton(self.Tabla)
        self.Btn_ordenarvel.setObjectName(u"Btn_ordenarvel")

        self.gridLayout.addWidget(self.Btn_ordenarvel, 2, 2, 1, 1)

        self.mostrar_button = QPushButton(self.Tabla)
        self.mostrar_button.setObjectName(u"mostrar_button")

        self.gridLayout.addWidget(self.mostrar_button, 1, 2, 1, 1)

        self.tabla_datos = QTableWidget(self.Tabla)
        self.tabla_datos.setObjectName(u"tabla_datos")

        self.gridLayout.addWidget(self.tabla_datos, 0, 0, 1, 3)

        self.Btn_ordenardis = QPushButton(self.Tabla)
        self.Btn_ordenardis.setObjectName(u"Btn_ordenardis")

        self.gridLayout.addWidget(self.Btn_ordenardis, 2, 1, 1, 1)

        self.tab_all.addTab(self.Tabla, "")
        self.Escena = QWidget()
        self.Escena.setObjectName(u"Escena")
        self.Escena_2 = QGraphicsView(self.Escena)
        self.Escena_2.setObjectName(u"Escena_2")
        self.Escena_2.setGeometry(QRect(0, 10, 571, 461))
        self.Dibujar = QPushButton(self.Escena)
        self.Dibujar.setObjectName(u"Dibujar")
        self.Dibujar.setGeometry(QRect(40, 490, 181, 31))
        self.Limpiar = QPushButton(self.Escena)
        self.Limpiar.setObjectName(u"Limpiar")
        self.Limpiar.setGeometry(QRect(340, 490, 211, 31))
        self.tab_all.addTab(self.Escena, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 667, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        self.tab_all.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.mostrar_datos.setText(QCoreApplication.translate("MainWindow", u"Mostrar datos", None))
        self.text_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.text_destinox.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.text_destinoy.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.text_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.text_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.text_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.text_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.btn_enviar_final.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"Agregar principio", None))
        self.tab_all.setTabText(self.tab_all.indexOf(self.agregar), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_button.setText(QCoreApplication.translate("MainWindow", u"buscar", None))
        self.Btn_ordenarid.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID", None))
        self.Btn_ordenarvel.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.mostrar_button.setText(QCoreApplication.translate("MainWindow", u"mostrar", None))
        self.Btn_ordenardis.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.tab_all.setTabText(self.tab_all.indexOf(self.Tabla), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tab_all.setTabText(self.tab_all.indexOf(self.Escena), QCoreApplication.translate("MainWindow", u"Escena", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

