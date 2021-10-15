

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys
import os

class Ui_IG5_Sena(object):

    def setupUi(self, IG5_Sena):
        IG5_Sena.setObjectName("IG5_Sena")
        IG5_Sena.resize(703, 693)
        self.nombreSena = QtWidgets.QLabel(IG5_Sena)
        self.nombreSena.setGeometry(QtCore.QRect(560, 40, 71, 21))
        self.nombreSena.setObjectName("nombreSena")
        self.widgetVideoTutorial = QtWidgets.QWidget(IG5_Sena)
        self.widgetVideoTutorial.setGeometry(QtCore.QRect(30, 30, 352, 640))
        self.widgetVideoTutorial.setObjectName("widgetVideoTutorial")
        self.botonReproducir = QtWidgets.QPushButton(IG5_Sena)
        self.botonReproducir.setGeometry(QtCore.QRect(550, 90, 75, 23))
        self.botonReproducir.setObjectName("botonReproducir")
        self.botonPausar = QtWidgets.QPushButton(IG5_Sena)
        self.botonPausar.setGeometry(QtCore.QRect(550, 140, 75, 23))
        self.botonPausar.setObjectName("botonPausar")
        self.botonVerificar = QtWidgets.QPushButton(IG5_Sena)
        self.botonVerificar.setGeometry(QtCore.QRect(600, 190, 81, 23))
        self.botonVerificar.setObjectName("botonVerificar")
        self.labelResultado = QtWidgets.QLabel(IG5_Sena)
        self.labelResultado.setGeometry(QtCore.QRect(470, 250, 221, 131))
        self.labelResultado.setText("")
        self.labelResultado.setObjectName("labelResultado")
        self.botonGrabar = QtWidgets.QPushButton(IG5_Sena)
        self.botonGrabar.setGeometry(QtCore.QRect(470, 190, 75, 23))
        self.botonGrabar.setObjectName("botonGrabar")
        self.labelTutorial = QtWidgets.QLabel(IG5_Sena)
        self.labelTutorial.setGeometry(QtCore.QRect(70, 10, 121, 16))
        self.labelTutorial.setObjectName("labelTutorial")

        # self.setup(IG5_Sena)

        self.retranslateUi(IG5_Sena)
        QtCore.QMetaObject.connectSlotsByName(IG5_Sena)
    def setNombre(self,nombre):
        self.nombreSena.setText(nombre)
    def retranslateUi(self, IG5_Sena):
        _translate = QtCore.QCoreApplication.translate
        IG5_Sena.setWindowTitle(_translate("IG5_Sena", "Form"))
        self.nombreSena.setText(_translate("IG5_Sena", "name"))
        self.botonReproducir.setText(_translate("IG5_Sena", "Reproducir"))
        self.botonPausar.setText(_translate("IG5_Sena", "Pausar"))
        self.botonVerificar.setText(_translate("IG5_Sena", "Verificar seña"))
        self.botonGrabar.setText(_translate("IG5_Sena", "Grabar seña"))
        self.labelTutorial.setText(_translate("IG5_Sena", "¿Cómo hacer la seña?"))

    def setup(self,Form):
        self.video = self.crearVideo(Form)
        self.video.show()
        self.contenedor = self.crearContenedor(Form)
        self.contenedor.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.path)))
        self.contenedor.play()
        self.eventos(Form)

    def crearContenedor(self,Form):
        contenedor = QtMultimedia.QMediaPlayer(Form)
        contenedor.setVideoOutput(self.video)
        return contenedor

    def crearVideo(self,Form):
        videoOutput = QtMultimediaWidgets.QVideoWidget(Form)
        caja = QtWidgets.QVBoxLayout()
        caja.addWidget(videoOutput)
        self.widgetVideoTutorial.setLayout(caja)
        return videoOutput

    def setPath(self,path):
        self.path = path

    def eventos(self,Form):
        self.botonReproducir.clicked.connect(self.contenedor.play)
        self.botonPausar.clicked.connect(self.contenedor.pause)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    IG5_Sena = QtWidgets.QWidget()
    ui = Ui_IG5_Sena()  
    ui.setupUi(IG5_Sena)
    IG5_Sena.show()
    sys.exit(app.exec_())
