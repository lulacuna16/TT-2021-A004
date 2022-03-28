from statistics import mode
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PIL import Image
# import Opencv para camara  -pip install opencv-python-
import cv2
import numpy as np
import glob
import tensorflow as tf
#redConv = tf.keras.models.load_model('./modeloNumerosEstaticos.h5')
# global redConv
global nombreSena
global contador
contador = 3
global leyendo
leyendo = False
global valido
valido = 0

redConvs = [tf.keras.models.load_model('./modeloNumerosEstaticos.h5'),tf.keras.models.load_model('./modeloAbecedario.h5')]
modelos = {
		0: ["1", "2", "3", "4", "5", "6", "7", "8"],
		1: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y"]
	}
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
	"    border-bottom: none;\n"
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
	"    border-bottom: none;\n"
	"}")
		self.botonPausar.setObjectName("botonPausar")
		self.botonVerificar = QtWidgets.QPushButton(IG5_Sena)
		self.botonVerificar.setGeometry(QtCore.QRect(560, 620, 121, 23))
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
	"    border-bottom: none;\n"
	"}")
		self.botonVerificar.setObjectName("botonVerificar")
		self.labelTutorial = QtWidgets.QLabel(IG5_Sena)
		self.labelTutorial.setGeometry(QtCore.QRect(80, 10, 309, 31))
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
	"    border-bottom: none;\n"
	"}")
		self.botonSalir.setObjectName("botonSalir")
		self.lblSenaCorrecta = QtWidgets.QLabel(IG5_Sena)
		self.lblSenaCorrecta.setGeometry(QtCore.QRect(520, 250, 161, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe Print")
		font.setPointSize(14)
		self.lblSenaCorrecta.setFont(font)
		self.lblSenaCorrecta.setStyleSheet("background-color: rgb(0, 170, 0);\n"
										   "color: rgb(255, 255, 255);\n"
										   "border-radius: 11px;\n"
										   "border:none;\n"
										   "border-left: 1px solid  rgb(0, 85, 0);\n"
										   "border-right: 1px solid  rgb(0, 85, 0);\n"
										   "border-bottom: 3px solid  rgb(0, 85, 0);")
		self.lblSenaCorrecta.setAlignment(QtCore.Qt.AlignCenter)
		self.lblSenaCorrecta.setObjectName("lblSenaCorrecta")
		self.labelConteo = QtWidgets.QLabel(IG5_Sena)
		self.labelConteo.setGeometry(QtCore.QRect(410, 320, 431, 291))
		self.labelConteo.setStyleSheet("background-color: rgb(170, 170, 255,0.4);\n"
								 "font: 180pt \"Segoe Print\";\n"
								 "\n"
								 "")
		self.labelConteo.setAlignment(QtCore.Qt.AlignCenter)
		self.labelConteo.setObjectName("labelConteo")
		self.labelVerificando = QtWidgets.QLabel(IG5_Sena)
		self.labelVerificando.setGeometry(QtCore.QRect(560, 620, 121, 23))
		self.labelVerificando.setStyleSheet("color: rgb(255, 255, 255);\n"
											"    font: 12pt \"Segoe Print\";\n"
											"    border-radius: 11px;\n"
											"    border:none;\n"
											"\n"
											"    border-left: 1px solid rgb rgb(63, 63, 63);\n"
											"    border-right: 1px solid rgb rgb(63, 63, 63);\n"
											"    border-bottom: 3px solid rgb rgb(108, 108, 108);\n"
											"\n"
											"background-color: rgb(149, 149, 149);")
		self.labelVerificando.setAlignment(QtCore.Qt.AlignCenter)
		self.labelVerificando.setObjectName("labelVerificando")

		self.lblCamara.raise_()
		self.lblSenaCorrecta.close()
		self.widgetVideoTutorial.raise_()
		self.botonReproducir.raise_()
		self.botonPausar.raise_()
		self.botonVerificar.raise_()
		self.labelTutorial.raise_()
		self.botonSalir.raise_()
		self.lblSenaCorrecta.raise_()
		self.labelConteo.raise_()
		self.labelConteo.close()
		self.labelVerificando.raise_()
		self.labelVerificando.close()

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
		self.lblSenaCorrecta.setText(_translate("IG5_Sena", "Seña correcta "))
		self.labelConteo.setText(_translate("IG5_Sena", "3"))
		self.labelVerificando.setText(_translate("IG5_Sena", "Verificando..."))

		# create a timer
		self.timer = QtCore.QTimer()

	def setNombre(self,nombre):
		global nombreSena
		nombreSena=nombre
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
		self.crearCamara()
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
		# set timer timeout callback function
		self.timer.timeout.connect(self.mostrarCamara)
		# set control_bt callback clicked  function
		# create video capture
		if not self.timer.isActive():
			#self.botonVerificar.setVisible(False)
			self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
			# start timer
			self.timer.start(20)

	# view camera
	def mostrarCamara(self):
		global leyendo, valido
		try:
			# read image in BGR format
			ret, image = self.cap.read()
			#conver image to RGBA format for the CNN
			NImage = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
			# convert image to RGB format
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			cv2.imwrite('Prueba.jpg', NImage)
			# get image infos
			height, width, channel = image.shape
			step = channel * width
			# create QImage from image
			qImg = QtGui.QImage(image.data, width, height, step, QtGui.QImage.Format_RGB888)
			# show image in img_label
			self.lblCamara.setPixmap(QtGui.QPixmap.fromImage(qImg))
			path = list(glob.glob('./*.jpg'))
			if leyendo:
				self.labelVerificando.show()
				self.botonVerificar.close()
				img_p = []
				image = Image.open(path[0])
				img_p.append(np.array(image.resize((300, 300))))
				img_prueba = np.array(img_p)
				if self.validacion(img_prueba):
					valido += 1
					if valido == 4:
						self.lblSenaCorrecta.show()
						self.botonVerificar.show()
						self.labelVerificando.close()
						self.terminar()
						#os.remove('./Prueba.jpg')
				else:
					valido = 0

		except Exception as error:
			print("No se detectó la cámara")
			print(error)

	def validacion(self,imagen):
		global nombreSena
		# global redConv
		m = 0
		for modelo, senas in modelos.items():
			if nombreSena in senas:
				redConv = redConvs[modelo]
				m = modelo
		global leyendo
		predicciones = redConv.predict(imagen)
		predicciones_etq = np.argmax(predicciones,axis=1)
		for i in predicciones_etq:
			prediccion = modelos[m][i]
			print(prediccion)
			if str(prediccion) == nombreSena:
				print("Seña correcta")
				return True
			else:
				print("Incorrecta")
				return False

	def terminar(self):
		global leyendo, valido
		if self.timer.isActive():
			# stop timer
			self.timer.stop()
			# release video capture
			self.cap.release()
		leyendo = False
		valido = 0
	def cerrar(self,Form):
		self.terminar()
		Form.close()

	def crearTimer(self):
		self.timerConteo = QtCore.QTimer()
		self.timerConteo.timeout.connect(self.iniciar_conteo)
		if not self.timerConteo.isActive():
			# start timer
			self.timerConteo.start(1000)

	def iniciar_conteo(self):
		global contador, leyendo
		self.lblSenaCorrecta.close()
		self.labelConteo.show()
		self.labelConteo.setText(str(contador))
		contador = contador-1
		# print(contador)
		if contador < 0:
			if self.timerConteo.isActive():
			# stop timer
				self.timerConteo.stop()
				self.labelConteo.close()
				contador=3
				leyendo = True
				if not self.timer.isActive():
					self.crearCamara()

	def eventos(self, Form):
		self.botonReproducir.clicked.connect(self.contenedor.play)
		self.botonPausar.clicked.connect(self.contenedor.pause)
		self.botonVerificar.clicked.connect(lambda:self.crearTimer())
		self.botonSalir.clicked.connect(lambda: self.cerrar(Form))

if __name__ == "__main__":
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	IG5_Sena = QtWidgets.QWidget()
	ui = Ui_IG5_Sena()
	ui.setupUi(IG5_Sena)
	IG5_Sena.show()
	sys.exit(app.exec_())
