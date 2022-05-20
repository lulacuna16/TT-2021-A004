from msilib.schema import tables
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PIL import Image
# import Opencv para camara  -pip install opencv-python-
import cv2
import numpy as np
import glob
import tensorflow as tf
from Clases.Senas import Senas
from Clases.Progreso import Progreso
import IG4 as G4
import os

#redConv = tf.keras.models.load_model('./modeloNumerosEstaticos.h5')
# global redConv
global nombreSena #Variable que permite utilizar el nombre de la seña para distintos propósitos
global contador #Variable para mostrar el contador en pantalla antes de comenzar la validación
contador = 3
global leyendoEstatica #Variable que indica que se está llevando a cabo la validación de la seña estatica
leyendoEstatica = False
global leyendoCiclo #Variable que indica que se está llevando a cabo la validación de la seña ciclica
leyendoCiclo = False
global leyendoDinamica #Variable que indica que se está llevando a cabo la validación de la seña dinámica cambiante
leyendoDinamica= False
global leyendoPatron #Variable que indica que se está llevando a cabo la validación de la seña dinámica cambiante con patrón 
leyendoPatron= False
global valido #Variable que nos permite contar las veces que la seña estática se ha realizado correctamente
valido = 0
global tiempoLectura #Variable que controla el tiempo que transcurre mientras se lee una seña.
tiempoLectura = 0
#Cada 3 unidades representan 1 segundo
tiempoLimiteE=60
tiempoLimiteD=90
global m, redConv #Variable para precargar el modelo para evaluar la seña
redConvs = [
	tf.keras.models.load_model('./modelos/modeloNumerosEstaticos.h5'),
	tf.keras.models.load_model('./modelos/modeloAbecedario_1.h5'),
	tf.keras.models.load_model('./modelos/modeloAbecedario_2.h5'),
	tf.keras.models.load_model('./modelos/modeloCuerpo.h5'),
	tf.keras.models.load_model('./modelos/modeloDias.h5'),
	tf.keras.models.load_model('./modelos/modeloNumeros307080.h5'),
	tf.keras.models.load_model('./modelos/modeloNumeros1020100.h5'),
	tf.keras.models.load_model('./modelos/modeloNumeros456.h5')
]
modelos = {
		0: ["1", "2", "3", "4", "5", "6", "7", "8"],
		1: ["A", "B", "C", "D", "E", "G", "I", "M", "R", "S"],
		2: ["F", "H", "L", "N", "O", "P", "T", "U", "V", "W", "Y"],
		3: ["Cuello", "Diente", "Espalda", "Estómago", "Hombro", "Lengua", "Mano", "Muñeca", "Nariz", "Pulgar", "Pelo"],
		4: ["Domingo", "Jueves", "Lunes", "Martes", "Miércoles", "Sábado","Viernes"],
		5: ["30", "70", "80"],
		6: ["10", "20", "100"],
		7: ["40", "50", "60"]
	}
Estatica = ["1", "2", "3", "4", "5", "6", "7", "8", "A", "B", "C", "D", "E", "G", "I", "M", "R", "S",
			"F", "H", "L", "N", "O", "P", "T", "U", "V", "W", "Y","Cuello", "Diente", "Espalda",
			"Estómago", "Hombro", "Lengua", "Mano", "Muñeca", "Nariz", "Pulgar", "Pelo"]
Ciclo = ["Domingo", "Jueves", "Lunes", "Martes", "Miércoles", "Sábado","Viernes"]
Patron = ["10", "20", "100", "30", "70", "80", "40", "50", "60"]

patrones = {
		"10": 	[2,3],
		"20":	[4,5,4,5,4,5],
		"100": 	[0,1],
		"30": 	[0,1,0,1,0,1],
		"70": 	[2,4,2,4,2,4],
		"80": 	[3,4,3,4,3,4]
	}
class Ui_IG5_Sena(object):
	def setupUi(self, IG5_Sena):
		IG5_Sena.setObjectName("IG5_Sena")
		IG5_Sena.resize(865, 693)
		IG5_Sena.setMaximumSize(QtCore.QSize(865, 693))
		IG5_Sena.setMinimumSize(QtCore.QSize(865, 693))
		IG5_Sena.setStyleSheet("background-color: rgb(250, 215, 160);\n"
"")
		self.widgetVideoTutorial = QtWidgets.QWidget(IG5_Sena)
		self.widgetVideoTutorial.setGeometry(QtCore.QRect(30, 50, 352, 640))
		self.widgetVideoTutorial.setObjectName("widgetVideoTutorial")
		self.botonReproducir = QtWidgets.QPushButton(IG5_Sena)
		self.botonReproducir.setGeometry(QtCore.QRect(470, 150, 101, 23))
		self.botonReproducir.setStyleSheet("QPushButton{\n"
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
"    background-color: rgb(40, 170, 221);\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-top: 3px solid rgb(44, 131, 212);\n"
"    border-bottomr: none;\n"
"}")
		self.botonPausar.setObjectName("botonPausar")
		self.botonVerificar = QtWidgets.QPushButton(IG5_Sena)
		self.botonVerificar.setGeometry(QtCore.QRect(560, 620, 121, 23))
		self.botonVerificar.setStyleSheet("QPushButton{\n"
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
"    background-color: rgb(40, 170, 221);\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-top: 3px solid rgb(44, 131, 212);\n"
"    border-bottomr: none;\n"
"}")
		self.botonVerificar.setObjectName("botonVerificar")
		self.labelTutorial = QtWidgets.QLabel(IG5_Sena)
		self.labelTutorial.setGeometry(QtCore.QRect(240, 10, 381, 31))
		self.labelTutorial.setStyleSheet("font: 16pt \"Segoe Print\";\n"
"color: rgb(156, 100, 12);")
		self.labelTutorial.setObjectName("labelTutorial")
		self.lblCamara = QtWidgets.QLabel(IG5_Sena)
		self.lblCamara.setGeometry(QtCore.QRect(410, 320, 431, 291))
		self.lblCamara.setText("")
		self.lblCamara.setObjectName("lblCamara")
		self.botonSalir = QtWidgets.QPushButton(IG5_Sena)
		self.botonSalir.setGeometry(QtCore.QRect(740, 10, 121, 23))
		self.botonSalir.setStyleSheet("QPushButton{\n"
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
"    background-color: rgb(40, 170, 221);\n"
"    border-left: 1px solid rgb(44, 131, 212);\n"
"    border-right: 1px solid rgb(44, 131, 212);\n"
"    border-top: 3px solid rgb(44, 131, 212);\n"
"    border-bottomr: none;\n"
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
"color: rgb(156, 100, 12);\n"
"font: 140pt \"MS Shell Dlg 2\";\n"
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

		self.labelInvalido = QtWidgets.QLabel(IG5_Sena)
		self.labelInvalido.setGeometry(QtCore.QRect(410, 320, 431, 291))
		self.labelInvalido.setStyleSheet("background-color: rgb(255, 0, 0,0.4);\n"
										 "font: 35pt \"Segoe Print\";\n"
										 "color: rgb(255, 255, 255);\n"
										 "QToolTip {\n" 
											"background-color: black;\n" 
										 	"color: white;\n" 
									        "border: black solid 1px;\n"
										 "}\n"
										 )
		self.labelInvalido.setAlignment(QtCore.Qt.AlignCenter)
		self.labelInvalido.setWordWrap(True)
		self.labelInvalido.setObjectName("labelInvalido")
		self.labelInvalido.setToolTip("Cuando una seña no se valida correctamente, puede ser por la poca o demasiada "
									  "ilumación del ambiente que no le permite a la cámara capturar su gesto adecuadamente. "
									  "Otras de las razones puede ser la distancia que hay entre la cámara y usted, cambie "
									  "dichos parámetros e intente de nuevo.")

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
		self.labelInvalido.raise_()
		self.labelInvalido.close()

		self.retranslateUi(IG5_Sena)
		QtCore.QMetaObject.connectSlotsByName(IG5_Sena)

	def retranslateUi(self, IG5_Sena):
		_translate = QtCore.QCoreApplication.translate
		IG5_Sena.setWindowTitle(_translate("IG5_Sena", "Aprendiendo seña"))
		IG5_Sena.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
		self.botonReproducir.setText(_translate("IG5_Sena", "Reproducir"))
		self.botonPausar.setText(_translate("IG5_Sena", "Pausar"))
		self.botonVerificar.setText(_translate("IG5_Sena", "Verificar seña"))
		self.labelTutorial.setText(_translate("IG5_Sena", "¿Cómo hacer la seña?"))
		self.botonSalir.setText(_translate("IG5_Sena", "Salir"))
		self.lblSenaCorrecta.setText(_translate("IG5_Sena", "Seña correcta "))
		self.labelConteo.setText(_translate("IG5_Sena", "3"))
		self.labelVerificando.setText(_translate("IG5_Sena", "Verificando..."))
		self.labelInvalido.setText(_translate("IG5_Sena", "No se pudo validar la seña, intente de nuevo."))
		self.labelInvalido.setToolTip(_translate("IG5_Sena",
		"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""background-color: rgb(255, 175, 247);\n""p, li { white-space: pre-wrap; }\n"
		"</style></head><body style=\" font-family:\'Segoe Print\'; font-size:35pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Cuando una seña no se valida correctamente, puede ser por la poca o demasiada ilumación del ambiente que no le permite a la cámara capturar su gesto adecuadamente. Otras de las razones puede ser la distancia que hay entre la cámara y usted, cambie dichos parámetros e intente de nuevo.</span></p></body></html>"))

		# create a timer
		self.timer = QtCore.QTimer()

	def setNombre(self,nombre):
		global nombreSena, m, redConv
		nombreSena=nombre
		self.labelTutorial.setText("¿Cómo hacer la seña \""+ nombre +"\" ?")
		for modelo, senas in modelos.items():
			if nombreSena in senas:
				redConv = redConvs[modelo]
				m = modelo

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
		global leyendoEstatica, leyendoCiclo, leyendoDinamica, valido, tiempoLectura, leyendoPatron
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
			if leyendoEstatica:
				self.validacionEstatica(path)
			if leyendoCiclo:
				self.validacionCiclo(path)
			if leyendoDinamica:
				self.validacionCiclo(path)
			if leyendoPatron:
				self.validacionPatron(path)


		except Exception as error:
			print("No se detectó la cámara")
			print(error)

	def comprobacion(self, imagen):
		global nombreSena, m, redConv

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

	def comprobacionPatron(self, imagen , valorEsperado):
		global nombreSena, m, redConv
		predicciones = redConv.predict(imagen)
		predicciones_etq = np.argmax(predicciones,axis=1)
		for i in predicciones_etq:
			# prediccion = modelos[m][i]
			print(i,valorEsperado)
			if i == valorEsperado:
				return True
			else:
				return False

	def validacionEstatica(self,path):
		global valido, tiempoLectura
		self.labelVerificando.show()
		self.botonVerificar.close()
		img_p = []
		image = Image.open(path[0])
		img_p.append(np.array(image.resize((300, 300))))
		img_prueba = np.array(img_p)
		tiempoLectura += 1
		if tiempoLectura < tiempoLimiteE:
			if self.comprobacion(img_prueba):
				valido += 1
				if valido == 4:
					self.lblSenaCorrecta.show()
					self.botonVerificar.show()
					self.labelVerificando.close()
					self.terminar()
					tiempoLectura=0
					#os.remove('./Prueba.jpg')

					pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
					sena = Senas()
					sena.setBD(pathBD)
					sena.nombre_sena = str(nombreSena).lower()
					sena.obtenerIdSenaBD()

					progreso = Progreso()
					progreso.setBD(pathBD)
					progreso.id_usuario = self.id_usuario
					progreso.id_sena = sena.id_sena
					progreso.insertarProgreso()

			else:
				valido = 0
		else:
			self.labelInvalido.show()
			print("No se pudo validar")
			self.botonVerificar.show()
			self.labelVerificando.close()
			self.reiniciar()
			tiempoLectura = 0

	def validacionCiclo(self,path):
		global valido, tiempoLectura
		self.labelVerificando.show()
		self.botonVerificar.close()
		img_p = []
		image = Image.open(path[0])
		img_p.append(np.array(image.resize((300, 300))))
		img_prueba = np.array(img_p)
		tiempoLectura += 1
		if tiempoLectura < tiempoLimiteD:
			if self.comprobacion(img_prueba):
				valido += 1
				if valido == 6:
					self.lblSenaCorrecta.show()
					self.botonVerificar.show()
					self.labelVerificando.close()
					self.terminar()
					tiempoLectura = 0
					# os.remove('./Prueba.jpg')

					pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/Clases/senas.db"
					sena = Senas()
					sena.setBD(pathBD)
					sena.nombre_sena = str(nombreSena).lower()
					sena.obtenerIdSenaBD()

					progreso = Progreso()
					progreso.setBD(pathBD)
					progreso.id_usuario = self.id_usuario
					progreso.id_sena = sena.id_sena
					progreso.insertarProgreso()
			else:
				valido = 0
		else:
			self.labelInvalido.show()
			print("No se pudo validar")
			self.botonVerificar.show()
			self.labelVerificando.close()
			self.reiniciar()
			tiempoLectura = 0

	def validacionPatron(self,path):
		global valido, tiempoLectura
		self.labelVerificando.show()
		self.botonVerificar.close()
		img_p = []
		image = Image.open(path[0])
		img_p.append(np.array(image.resize((300, 300))))
		img_prueba = np.array(img_p)
		tiempoLectura += 1
		print(valido)
		# if tiempoLectura < tiempoLimiteD:
		if self.comprobacionPatron(img_prueba,patrones[nombreSena][valido]):
			valido += 1
			print('vi un lindo gatito')

			if valido == len(patrones[nombreSena]):
				self.lblSenaCorrecta.show()
				self.botonVerificar.show()
				self.labelVerificando.close()
				self.terminar()
				tiempoLectura = 0
				# os.remove('./Prueba.jpg')

				pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/Clases/senas.db"
				sena = Senas()
				sena.setBD(pathBD)
				sena.nombre_sena = str(nombreSena).lower()
				sena.obtenerIdSenaBD()

				progreso = Progreso()
				progreso.setBD(pathBD)
				progreso.id_usuario = self.id_usuario
				progreso.id_sena = sena.id_sena
				progreso.insertarProgreso()
		# else:
		# 	self.labelInvalido.show()
		# 	print("No se pudo validar")
		# 	self.botonVerificar.show()
		# 	self.labelVerificando.close()
		# 	self.reiniciar()
		# 	tiempoLectura = 0

	def terminar(self):
		if self.timer.isActive():
			# stop timer
			self.timer.stop()
			# release video capture
			self.cap.release()
		self.reiniciar()

	def reiniciar(self):
		global leyendoEstatica, leyendoCiclo, leyendoDinamica, valido, leyendoPatron
		leyendoEstatica = False
		leyendoCiclo = False
		leyendoDinamica = False
		leyendoPatron = False
		valido = 0

	def cerrar(self,Form):
		self.terminar()
		Form.close()
		self.abrirIG4(Form)

	def crearTimer(self):
		self.timerConteo = QtCore.QTimer()
		self.timerConteo.timeout.connect(self.iniciar_conteo)
		if not self.timerConteo.isActive():
			# start timer
			self.timerConteo.start(1000)

	def iniciar_conteo(self):
		global contador, leyendoEstatica, leyendoCiclo, leyendoDinamica, nombreSena, leyendoPatron
		self.lblSenaCorrecta.close()
		self.labelInvalido.close()
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
				if nombreSena in Estatica:
					leyendoEstatica = True
				if nombreSena in Ciclo:
					leyendoCiclo = True
				if nombreSena in Patron:
					leyendoPatron = True
				"""if nombreSena in Dinamica:
					leyendoDinamica = True"""
				if not self.timer.isActive():
					self.crearCamara()

	def eventos(self, Form):
		self.botonReproducir.clicked.connect(self.contenedor.play)
		self.botonPausar.clicked.connect(self.contenedor.pause)
		self.botonVerificar.clicked.connect(lambda:self.crearTimer())
		self.botonSalir.clicked.connect(lambda: self.cerrar(Form))

	def setIDUsuario(self,id_usuario):
		self.id_usuario = id_usuario

	def abrirIG4(self,IG5_Sena):
		pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
		sena = Senas()
		sena.setBD(pathBD)
		sena.nombre_sena = str(nombreSena).lower()
		print(sena.nombre_sena)
		sena.obtenerIdSenaBD()

		IG5_Sena.hide()
		self.IIG4=QtWidgets.QWidget()
		ui=G4.Ui_IG4_Aprendizaje()
		ui.setIDUsuario(self.id_usuario)
		ui.setupUi(self.IIG4)
		ui.Tabs.setCurrentIndex(sena.id_categoria)
		self.IIG4.show()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	IG5_Sena = QtWidgets.QWidget()
	ui = Ui_IG5_Sena()
	ui.setupUi(IG5_Sena)
	IG5_Sena.show()
	sys.exit(app.exec_())
