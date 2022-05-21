# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\IG6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import IG7 as G7
import IG2 as G2
from Clases.Practica import Practica
import os

class Ui_IG6_SeccionPractica(object):
	def setupUi(self, IG6_SeccionPractica):
		IG6_SeccionPractica.setObjectName("IG6_SeccionPractica")
		IG6_SeccionPractica.setMaximumSize(QtCore.QSize(817, 482))
		IG6_SeccionPractica.setMinimumSize(QtCore.QSize(817, 482))
		IG6_SeccionPractica.setStyleSheet("QWidget{\n"
"background-color: rgb(250, 215, 160);\n"
"}\n"
"")
		self.label_instruccion = QtWidgets.QLabel(IG6_SeccionPractica)
		self.label_instruccion.setGeometry(QtCore.QRect(70, 0, 681, 131))
		self.label_instruccion.setStyleSheet("font: 26pt \"Segoe Print\";\n"
"background-color: rgb(250, 215, 160);\n"
"color: rgb(156, 100, 12);\n"
"qproperty-alignment: AlignCenter;")
		self.label_instruccion.setObjectName("label_instruccion")
		self.gridLayoutWidget = QtWidgets.QWidget(IG6_SeccionPractica)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 160, 541, 231))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.boton_abecedario = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.boton_abecedario.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_abecedario.setObjectName("boton_abecedario")
		self.gridLayout.addWidget(self.boton_abecedario, 0, 0, 1, 1)
		self.boton_numeros = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.boton_numeros.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_numeros.setObjectName("boton_numeros")
		self.gridLayout.addWidget(self.boton_numeros, 0, 2, 1, 1)
		self.boton_cuerpo = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.boton_cuerpo.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_cuerpo.setObjectName("boton_cuerpo")
		self.gridLayout.addWidget(self.boton_cuerpo, 1, 1, 1, 1)
		self.boton_dias = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.boton_dias.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_dias.setObjectName("boton_dias")
		self.gridLayout.addWidget(self.boton_dias, 2, 0, 1, 1)
		self.boton_colores = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.boton_colores.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_colores.setObjectName("boton_colores")
		self.gridLayout.addWidget(self.boton_colores, 2, 2, 1, 1)
		self.boton_regresar = QtWidgets.QPushButton(IG6_SeccionPractica)
		self.boton_regresar.setGeometry(QtCore.QRect(330, 430, 151, 31))
		self.boton_regresar.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 100, 12);\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 11px;\n"
"    border:none;\n"
"    border-left: 1px solid rgb(156, 100, 12);\n"
"    border-right: 1px solid rgb(156, 100, 12);\n"
"    border-bottom: 3px solid rgb(156, 100, 12);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(248, 196, 113);\n"
"    border-left: 1px solid rgb(248, 196, 113);\n"
"    border-right: 1px solid rgb(248, 196, 113);\n"
"    border-bottom: 3px solid rgb(248, 196, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(120, 66, 18);\n"
"    border-left: 1px solid  rgb(120, 66, 18);\n"
"    border-right: 1px solid  rgb(120, 66, 18);\n"
"    border-top: 3px solid  rgb(120, 66, 18);\n"
"    border-bottom: none;\n"
"}")
		self.boton_regresar.setObjectName("boton_regresar")

		self.eventos(IG6_SeccionPractica)

		self.retranslateUi(IG6_SeccionPractica)
		QtCore.QMetaObject.connectSlotsByName(IG6_SeccionPractica)

	def retranslateUi(self, IG6_SeccionPractica):
		_translate = QtCore.QCoreApplication.translate
		IG6_SeccionPractica.setWindowTitle(_translate("IG6_SeccionPractica", "Menú de práctica"))
		self.label_instruccion.setText(_translate("IG6_SeccionPractica", "Selecciona categoría"))
		self.boton_abecedario.setText(_translate("IG6_SeccionPractica", "Abecedario"))
		self.boton_numeros.setText(_translate("IG6_SeccionPractica", "Números"))
		self.boton_cuerpo.setText(_translate("IG6_SeccionPractica", "Cuerpo"))
		self.boton_dias.setText(_translate("IG6_SeccionPractica", "Días"))
		self.boton_colores.setText(_translate("IG6_SeccionPractica", "Colores"))
		self.boton_regresar.setText(_translate("IG6_SeccionPractica", "Regresar"))

	def eventos(self,IG6):
		self.boton_abecedario.clicked.connect(lambda: self.abrirIG7(IG6,1))
		self.boton_numeros.clicked.connect(lambda: self.abrirIG7(IG6,2))
		self.boton_cuerpo.clicked.connect(lambda: self.abrirIG7(IG6,3))
		self.boton_dias.clicked.connect(lambda: self.abrirIG7(IG6,4))
		self.boton_colores.clicked.connect(lambda: self.abrirIG7(IG6,5))
		self.boton_regresar.clicked.connect(lambda: self.abrirIG2(IG6))

	def setIDUsuario(self,id):
		self.id_usuario = id

	def abrirIG7(self,IG6,categoria):
		IG6.hide()
		self.IG7_Test = QtWidgets.QWidget()
		ui = G7.Ui_IG7_test()

		#Crear cuestionario
		cuestionario = Practica()
		path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
		cuestionario.setBD(path)
		cuestionario.id_categoria = categoria
		cuestionario.crearPreguntas()

		ui.setCuestionario(cuestionario)
		ui.setIDUsuario(self.id_usuario)
		ui.setupUi(self.IG7_Test)
		self.IG7_Test.show()

	def abrirIG2(self,IG6):
		IG6.hide()
		self.IIG2=QtWidgets.QWidget()
		ui = G2.Ui_IG2_MenuUsuario()
		ui.setIDUsuario(self.id_usuario)
		ui.setupUi(self.IIG2)
		self.IIG2.show()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	IG6_SeccionPractica = QtWidgets.QWidget()
	ui = Ui_IG6_SeccionPractica()
	ui.setupUi(IG6_SeccionPractica)
	ui.setIDUsuario(1)
	IG6_SeccionPractica.show()
	sys.exit(app.exec_())
