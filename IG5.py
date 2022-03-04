# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\IG5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys
import os
# import Opencv para camara  -pip install opencv-python-
import cv2

class Ui_IG5_Sena(object):
	def setupUi(self, IG5_Sena):
		IG5_Sena.setObjectName("IG5_Sena")
		IG5_Sena.resize(865, 693)
		IG5_Sena.setStyleSheet("    background-color: rgb(255, 149, 250);\n"
	"")
		self.widgetVideoTutorial = QtWidgets.QWidget(IG5_Sena)
		self.widgetVideoTutorial.setGeometry(QtCore.QRect(30, 50, 352, 640))
		self.widgetVideoTutorial.setObjectName("widgetVideoTutorial")
		self.botonReproducir = QtWidgets.QPushButton(IG5_Sena)
		self.botonReproducir.setGeometry(QtCore.QRect(470, 150, 101, 23))
		self.botonReproducir.setStyleSheet("QPushButton{\n"
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
	"    border-bottomr: none;\n"
	"}")
		self.botonReproducir.setObjectName("botonReproducir")
		self.botonPausar = QtWidgets.QPushButton(IG5_Sena)
		self.botonPausar.setGeometry(QtCore.QRect(680, 150, 101, 23))
		self.botonPausar.setStyleSheet("QPushButton{\n"
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
	"    border-bottomr: none;\n"
	"}")
		self.botonPausar.setObjectName("botonPausar")
		self.botonVerificar = QtWidgets.QPushButton(IG5_Sena)
		self.botonVerificar.setGeometry(QtCore.QRect(560, 450, 121, 23))
		self.botonVerificar.setStyleSheet("QPushButton{\n"
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
	"    border-bottomr: none;\n"
	"}")
		self.botonVerificar.setObjectName("botonVerificar")
		self.labelTutorial = QtWidgets.QLabel(IG5_Sena)
		self.labelTutorial.setGeometry(QtCore.QRect(80, 10, 241, 31))
		self.labelTutorial.setStyleSheet("font: 16pt \"Segoe Print\";")
		self.labelTutorial.setObjectName("labelTutorial")
		self.lblCamara = QtWidgets.QLabel(IG5_Sena)
		self.lblCamara.setGeometry(QtCore.QRect(410, 320, 431, 291))
		self.lblCamara.setText("")
		self.lblCamara.setObjectName("lblCamara")
		self.botonSalir = QtWidgets.QPushButton(IG5_Sena)
		self.botonSalir.setGeometry(QtCore.QRect(740, 10, 121, 23))
		self.botonSalir.setStyleSheet("QPushButton{\n"
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
	"    border-bottomr: none;\n"
	"}")
		self.botonSalir.setObjectName("botonSalir")
		self.lblCamara.raise_()
		self.widgetVideoTutorial.raise_()
		self.botonReproducir.raise_()
		self.botonPausar.raise_()
		self.botonVerificar.raise_()
		self.labelTutorial.raise_()
		self.botonSalir.raise_()

		self.retranslateUi(IG5_Sena)
		QtCore.QMetaObject.connectSlotsByName(IG5_Sena)

	def retranslateUi(self, IG5_Sena):
		_translate = QtCore.QCoreApplication.translate
		IG5_Sena.setWindowTitle(_translate("IG5_Sena", "Form"))
		IG5_Sena.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
		self.botonReproducir.setText(_translate("IG5_Sena", "Reproducir"))
		self.botonPausar.setText(_translate("IG5_Sena", "Pausar"))
		self.botonVerificar.setText(_translate("IG5_Sena", "Verificar seña"))
		self.labelTutorial.setText(_translate("IG5_Sena", "¿Cómo hacer la seña?"))
		self.botonSalir.setText(_translate("IG5_Sena", "Salir"))

	def setNombre(self,nombre):
		self.labelTutorial.setText("¿Cómo hacer la seña \""+ nombre +"\" ?")

	def setup(self, Form):
		self.video = self.crearVideo(Form)
		self.video.show()
		self.contenedor = self.crearContenedor(Form)
		self.contenedor.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.path)))
		self.contenedor.play()
		self.eventos(Form)

	def crearContenedor(self, Form):
		contenedor = QtMultimedia.QMediaPlayer(Form)
		contenedor.setVideoOutput(self.video)
		return contenedor

	def crearVideo(self, Form):
		videoOutput = QtMultimediaWidgets.QVideoWidget(Form)
		caja = QtWidgets.QVBoxLayout()
		caja.addWidget(videoOutput)
		self.widgetVideoTutorial.setLayout(caja)
		return videoOutput

	def setPath(self, path):
		self.path = path

	def crearCamara(self):
		# create a timer
		self.timer = QtCore.QTimer()
		# set timer timeout callback function
		self.timer.timeout.connect(self.mostrarCamara)
		# set control_bt callback clicked  function
		# create video capture
		if not self.timer.isActive():
			self.botonVerificar.setVisible(False)
			self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
			# start timer
			self.timer.start(20)

	# view camera
	def mostrarCamara(self):
		try:
			# read image in BGR format
			ret, image = self.cap.read()
			# convert image to RGB format
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			# get image infos
			height, width, channel = image.shape
			step = channel * width
			# create QImage from image
			qImg = QtGui.QImage(image.data, width, height, step, QtGui.QImage.Format_RGB888)
			# show image in img_label
			self.lblCamara.setPixmap(QtGui.QPixmap.fromImage(qImg))
		except Exception as error:
			print("No se detecto la camara")
			print(error)


	def cerrar(self,Form):
		if self.timer.isActive():
			# stop timer
			self.timer.stop()
			# release video capture
			self.cap.release()
		Form.close()

	def eventos(self, Form):
		self.botonReproducir.clicked.connect(self.contenedor.play)
		self.botonPausar.clicked.connect(self.contenedor.pause)
		self.botonVerificar.clicked.connect(lambda: self.crearCamara())
		self.botonSalir.clicked.connect(lambda: self.cerrar(Form))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	IG5_Sena = QtWidgets.QWidget()
	ui = Ui_IG5_Sena()
	ui.setupUi(IG5_Sena)
	IG5_Sena.show()
	sys.exit(app.exec_())
