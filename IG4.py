# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG4.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import IG4_1_Abecedario as abecedario
import IG4_2_Numeros as numeros
import IG4_3_Cuerpo as cuerpo
import IG4_4_Dias as dias
import IG4_5_Colores as colores
import IG2 as G2
from Clases.Usuario import Usuario
import os
from os import environ
from Clases.Progreso import Progreso

class Ui_IG4_Aprendizaje(object):
    def setupUi(self, IG4_Aprendizaje):
        IG4_Aprendizaje.setObjectName("IG4_Aprendizaje")
        IG4_Aprendizaje.resize(874, 492)
        font = QtGui.QFont()
        font.setPointSize(-1)
        IG4_Aprendizaje.setFont(font)
        IG4_Aprendizaje.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 149, 250);\n"
"    \n"
"    font-size: 15px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(IG4_Aprendizaje)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Tabs = QtWidgets.QTabWidget(IG4_Aprendizaje)
        font = QtGui.QFont()
        font.setFamily("Croissant One")
        font.setPointSize(-1)
        self.Tabs.setFont(font)
        self.Tabs.setStyleSheet("QTabWidget{\n"
"    font-family: \"Croissant One\";\n"
"}")
        self.Tabs.setObjectName("Tabs")
        self.tabInicio = QtWidgets.QWidget()
        self.tabInicio.setObjectName("tabInicio")
        self.gridLayout = QtWidgets.QGridLayout(self.tabInicio)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.tabInicio)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.botonRegresar = QtWidgets.QPushButton(self.frame_2)
        self.botonRegresar.setGeometry(QtCore.QRect(330, 310, 151, 41))
        self.botonRegresar.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(46, 165, 255);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-bottom: 3px solid rgb(44, 131, 212);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(14, 235, 255);\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-bottom: 3px solid rgb(44, 131, 212);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(40, 170, 221);\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-top: 3px solid rgb(44, 131, 212);\n"
"    border-bottom: none;\n"
"}")
        self.botonRegresar.setObjectName("botonRegresar")
        self.label_37 = QtWidgets.QLabel(self.frame_2)
        self.label_37.setGeometry(QtCore.QRect(50, 10, 721, 251))
        self.label_37.setStyleSheet("font: 24pt \"Segoe Print\";")
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.Tabs.addTab(self.tabInicio, "")
        self.tabAbecedario = QtWidgets.QWidget()
        self.tabAbecedario.setObjectName("tabAbecedario")
        self.widgetAbecedario = QtWidgets.QWidget(self.tabAbecedario)
        self.widgetAbecedario.setGeometry(QtCore.QRect(10, 60, 831, 311))
        self.widgetAbecedario.setObjectName("widgetAbecedario")
        ventanaAbecedario = abecedario.IG_Abecedario()
        ventanaAbecedario.iniciar_Abecedario(self.widgetAbecedario)
        ventanaAbecedario.retranslateUiAbecedario(IG4_Aprendizaje)
        self.Tabs.addTab(self.tabAbecedario, "")

        self.tabNumeros = QtWidgets.QWidget()
        self.tabNumeros.setObjectName("tabNumeros")
        self.widgetNumeros = QtWidgets.QWidget(self.tabNumeros)
        self.widgetNumeros.setGeometry(QtCore.QRect(0, 60, 841, 311))
        self.widgetNumeros.setObjectName("widgetNumeros")
        ventanaNumeros = numeros.IG_Numeros()
        ventanaNumeros.iniciar_Numeros(self.widgetNumeros)
        ventanaNumeros.retranslateUi(IG4_Aprendizaje)
        self.Tabs.addTab(self.tabNumeros, "")

        self.tabCuerpo = QtWidgets.QWidget()
        self.tabCuerpo.setObjectName("tabCuerpo")
        self.widgetCuerpo = QtWidgets.QWidget(self.tabCuerpo)
        self.widgetCuerpo.setGeometry(QtCore.QRect(40, 60, 741, 311))
        self.widgetCuerpo.setObjectName("widgetCuerpo")
        ventanaCuerpo = cuerpo.IG_Cuerpo()
        ventanaCuerpo.iniciar_Cuerpo(self.widgetCuerpo)
        ventanaCuerpo.retranslateUiCuerpo(IG4_Aprendizaje)
        self.Tabs.addTab(self.tabCuerpo, "")

        self.tabDias = QtWidgets.QWidget()
        self.tabDias.setObjectName("tabDias")
        self.widgetDias = QtWidgets.QWidget(self.tabDias)
        self.widgetDias.setGeometry(QtCore.QRect(10, 100, 761, 241))
        self.widgetDias.setObjectName("widgetDias")
        ventanaDias = dias.IG_Dias()
        ventanaDias.iniciar_Dias(self.widgetDias)
        ventanaDias.retranslateUiDias(IG4_Aprendizaje)
        self.Tabs.addTab(self.tabDias, "")

        self.tabColores = QtWidgets.QWidget()
        self.tabColores.setObjectName("tabColores")
        self.widgetColores = QtWidgets.QWidget(self.tabColores)
        self.widgetColores.setGeometry(QtCore.QRect(40, 60, 784, 311))
        self.widgetColores.setObjectName("widgetColores")
        ventanaColores = colores.IG_Colores()
        ventanaColores.iniciar_Colores(self.widgetColores)
        ventanaColores.retranslateUiColores(IG4_Aprendizaje)
        self.Tabs.addTab(self.tabColores, "")

        # BARRAS DE PROGRESO
        styleProgressBar ='''
                        QProgressBar{
                            text-align: center;
                            font: 12pt Segoe Print;
                            font-weight: bold;
                            color: black;
                            min-height: 20px;
                            max-height: 20px;
                            border-radius: 6px;
                            border: 1px solid #009688;
                            background-color: #EFEFEF;
                        }
                        QProgressBar::chunk{
                            border-radius: 6px;
                            background-color: #009688;
                        }
        '''
        self.progressBar_abecedario = QtWidgets.QProgressBar(self.tabAbecedario)
        self.progressBar_abecedario.setGeometry(QtCore.QRect(20, 20, 811, 22))
        self.progressBar_abecedario.setStyleSheet(styleProgressBar)
        self.progressBar_abecedario.setProperty("value", 0)
        self.progressBar_abecedario.setObjectName("progressBar_abecedario")

        self.progressBar_numeros = QtWidgets.QProgressBar(self.tabNumeros)
        self.progressBar_numeros.setGeometry(QtCore.QRect(20, 20, 811, 22))
        self.progressBar_numeros.setStyleSheet(styleProgressBar)
        self.progressBar_numeros.setProperty("value", 0)
        self.progressBar_numeros.setObjectName("progressBar_numeros")

        self.progressBar_cuerpo = QtWidgets.QProgressBar(self.tabCuerpo)
        self.progressBar_cuerpo.setGeometry(QtCore.QRect(20, 20, 811, 22))
        self.progressBar_cuerpo.setStyleSheet(styleProgressBar)
        self.progressBar_cuerpo.setProperty("value", 0)
        self.progressBar_cuerpo.setObjectName("progressBar_cuerpo")

        self.progressBar_dias = QtWidgets.QProgressBar(self.tabDias)
        self.progressBar_dias.setGeometry(QtCore.QRect(20, 20, 811, 22))
        self.progressBar_dias.setStyleSheet(styleProgressBar)
        self.progressBar_dias.setProperty("value", 0)
        self.progressBar_dias.setObjectName("progressBar_dias")

        self.progressBar_colores = QtWidgets.QProgressBar(self.tabColores)
        self.progressBar_colores.setGeometry(QtCore.QRect(20, 20, 811, 22))
        self.progressBar_colores.setStyleSheet(styleProgressBar)
        self.progressBar_colores.setProperty("value", 0)
        self.progressBar_colores.setObjectName("progressBar_colores")

        progreso = Progreso()
        pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        progreso = Progreso()
        progreso.setBD(pathBD)
        porcentaje = progreso.progresoCategoria(1,1)
        self.progressBar_abecedario.setValue(porcentaje)
        porcentaje = progreso.progresoCategoria(1,2)
        self.progressBar_numeros.setValue(porcentaje)
        porcentaje = progreso.progresoCategoria(1,3)
        self.progressBar_cuerpo.setValue(porcentaje)
        porcentaje = progreso.progresoCategoria(1,4)
        self.progressBar_dias.setValue(porcentaje)
        porcentaje = progreso.progresoCategoria(1,5)
        self.progressBar_colores.setValue(porcentaje)

        self.verticalLayout.addWidget(self.Tabs)
        self.Eventos(IG4_Aprendizaje)

        self.retranslateUi(IG4_Aprendizaje)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IG4_Aprendizaje)
    def abrirIG2(self,IG4_Aprendizaje):
        IG4_Aprendizaje.hide()
        self.IIG2=QtWidgets.QWidget()
        ui=G2.Ui_IG2_MenuUsuario()
        ui.setupUi(self.IIG2)
        self.IIG2.show()
    def Eventos(self,IG4_Aprendizaje):
        self.botonRegresar.clicked.connect(lambda:self.abrirIG2(IG4_Aprendizaje))

    def nombreUsuario(self,id):
        usuario = Usuario()
        path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        usuario.setBD(path)
        usuario.obtenerUsuarioBDId(id)
        return usuario.nombre

    def retranslateUi(self, IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Menú de aprendizaje"))
        self.botonRegresar.setText(_translate("IG4_Aprendizaje", "Regresar"))
        self.label_37.setText(_translate("IG4_Aprendizaje", "Bienvenido al menú de Aprendizaje\n"
"Presiona sobre una categoría para ver \n"
"las señas disponibles"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabInicio), _translate("IG4_Aprendizaje", "Inicio"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabAbecedario), _translate("IG4_Aprendizaje", "Abecedario"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabNumeros), _translate("IG4_Aprendizaje", "Números"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabCuerpo), _translate("IG4_Aprendizaje", "Cuerpo"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabDias), _translate("IG4_Aprendizaje", "Días"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabColores), _translate("IG4_Aprendizaje", "Colores"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IG4_Aprendizaje = QtWidgets.QWidget()
    ui = Ui_IG4_Aprendizaje()
    ui.setupUi(IG4_Aprendizaje)
    IG4_Aprendizaje.show()
    sys.exit(app.exec_())
