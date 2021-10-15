from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
import os

class IG_Cuerpo(object):
    def iniciar_Cuerpo(self, widgetCuerpo):
        self.imagen_Ojo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Ojo.setGeometry(QtCore.QRect(190, 220, 51, 41))
        self.imagen_Ojo.setObjectName("imagen_Ojo")
        self.boton_Ojo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Ojo.setGeometry(QtCore.QRect(180, 270, 75, 23))
        self.boton_Ojo.setObjectName("boton_Ojo")
        """self.imagen_Boca = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Boca.setGeometry(QtCore.QRect(130, 20, 51, 41))
        self.imagen_Boca.setObjectName("imagen_Boca")
        self.boton_Boca = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Boca.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.boton_Boca.setObjectName("boton_Boca")
        self.imagen_Brazo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Brazo.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.imagen_Brazo.setObjectName("imagen_Brazo")
        self.boton_Brazo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Brazo.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.boton_Brazo.setObjectName("boton_Brazo")
        self.imagen_Codo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Codo.setGeometry(QtCore.QRect(320, 20, 51, 41))
        self.imagen_Codo.setObjectName("imagen_Codo")
        self.boton_Codo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Codo.setGeometry(QtCore.QRect(310, 70, 75, 23))
        self.boton_Codo.setObjectName("boton_Codo")"""
        self.imagen_Cuello = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Cuello.setGeometry(QtCore.QRect(420, 20, 51, 41))
        self.imagen_Cuello.setObjectName("imagen_Cuello")
        self.boton_Cuello = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Cuello.setGeometry(QtCore.QRect(410, 70, 75, 23))
        self.boton_Cuello.setObjectName("boton_Cuello")
        self.imagen_Diente = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Diente.setGeometry(QtCore.QRect(520, 20, 51, 41))
        self.imagen_Diente.setObjectName("imagen_Diente")
        self.boton_Diente = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Diente.setGeometry(QtCore.QRect(510, 70, 75, 23))
        self.boton_Diente.setObjectName("boton_Diente")
        self.imagen_Espalda = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Espalda.setGeometry(QtCore.QRect(620, 20, 51, 41))
        self.imagen_Espalda.setObjectName("imagen_Espalda")
        self.boton_Espalda = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Espalda.setGeometry(QtCore.QRect(610, 70, 75, 23))
        self.boton_Espalda.setObjectName("boton_Espalda")
        self.imagen_Una = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Una.setGeometry(QtCore.QRect(550, 220, 51, 41))
        self.imagen_Una.setObjectName("imagen_Una")
        self.boton_Una = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Una.setGeometry(QtCore.QRect(540, 270, 75, 23))
        self.boton_Una.setObjectName("boton_Una")
        """self.imagen_Oreja = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Oreja.setGeometry(QtCore.QRect(280, 220, 51, 41))
        self.imagen_Oreja.setObjectName("imagen_Oreja")
        self.boton_Oreja = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Oreja.setGeometry(QtCore.QRect(270, 270, 75, 23))
        self.boton_Oreja.setObjectName("boton_Oreja")"""
        self.imagen_Estomago = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Estomago.setGeometry(QtCore.QRect(130, 120, 51, 41))
        self.imagen_Estomago.setObjectName("imagen_Estomago")
        self.boton_Estomago = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Estomago.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.boton_Estomago.setObjectName("boton_Estomago")
        self.imagen_Hombro = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Hombro.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_Hombro.setObjectName("imagen_Hombro")
        self.boton_Hombro = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Hombro.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.boton_Hombro.setObjectName("boton_Hombro")
        self.imagen_Lengua = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Lengua.setGeometry(QtCore.QRect(320, 120, 51, 41))
        self.imagen_Lengua.setObjectName("imagen_Lengua")
        self.boton_Lengua = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Lengua.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.boton_Lengua.setObjectName("boton_Lengua")
        self.imagen_Mano = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Mano.setGeometry(QtCore.QRect(420, 120, 51, 41))
        self.imagen_Mano.setObjectName("imagen_Mano")
        self.boton_Mano = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Mano.setGeometry(QtCore.QRect(410, 170, 75, 23))
        self.boton_Mano.setObjectName("boton_Mano")
        self.imagen_Muneca = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Muneca.setGeometry(QtCore.QRect(520, 120, 51, 41))
        self.imagen_Muneca.setObjectName("imagen_Muneca")
        self.boton_Muneca = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Muneca.setGeometry(QtCore.QRect(510, 170, 75, 23))
        self.boton_Muneca.setObjectName("boton_Muneca")
        self.imagen_Nariz = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Nariz.setGeometry(QtCore.QRect(620, 120, 51, 41))
        self.imagen_Nariz.setObjectName("imagen_Nariz")
        self.boton_Nariz = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Nariz.setGeometry(QtCore.QRect(610, 170, 75, 23))
        self.boton_Nariz.setObjectName("boton_Nariz")
        self.imagen_Pulgar = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Pulgar.setGeometry(QtCore.QRect(460, 220, 51, 41))
        self.imagen_Pulgar.setObjectName("imagen_Pulgar")
        self.boton_Pulgar = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Pulgar.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.boton_Pulgar.setObjectName("boton_Pulgar")
        self.imagen_Pelo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Pelo.setGeometry(QtCore.QRect(370, 220, 51, 41))
        self.imagen_Pelo.setObjectName("imagen_Pelo")
        self.boton_Pelo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Pelo.setGeometry(QtCore.QRect(360, 270, 75, 23))
        self.boton_Pelo.setObjectName("boton_Pelo")

        #self.boton_Boca.clicked.connect(lambda: self.buttonClicked(self.boton_Boca))
        #self.boton_Brazo.clicked.connect(lambda: self.buttonClicked(self.boton_Brazo))
        #self.boton_Codo.clicked.connect(lambda: self.buttonClicked(self.boton_Codo))
        self.boton_Cuello.clicked.connect(lambda: self.buttonClicked(self.boton_Cuello))
        self.boton_Diente.clicked.connect(lambda: self.buttonClicked(self.boton_Diente))
        self.boton_Espalda.clicked.connect(lambda: self.buttonClicked(self.boton_Espalda))
        self.boton_Estomago.clicked.connect(lambda: self.buttonClicked(self.boton_Estomago))
        self.boton_Hombro.clicked.connect(lambda: self.buttonClicked(self.boton_Hombro))
        self.boton_Lengua.clicked.connect(lambda: self.buttonClicked(self.boton_Lengua))
        self.boton_Mano.clicked.connect(lambda: self.buttonClicked(self.boton_Mano))
        self.boton_Muneca.clicked.connect(lambda: self.buttonClicked(self.boton_Muneca))
        self.boton_Nariz.clicked.connect(lambda: self.buttonClicked(self.boton_Nariz))
        self.boton_Ojo.clicked.connect(lambda: self.buttonClicked(self.boton_Ojo))
        #self.boton_Oreja.clicked.connect(lambda: self.buttonClicked(self.boton_Oreja))
        self.boton_Pelo.clicked.connect(lambda: self.buttonClicked(self.boton_Pelo))
        self.boton_Pulgar.clicked.connect(lambda: self.buttonClicked(self.boton_Pulgar))
        self.boton_Una.clicked.connect(lambda: self.buttonClicked(self.boton_Una))
    def buttonClicked(self, boton):
        self.IIG5=QtWidgets.QWidget()
        Sena = IGSena.Ui_IG5_Sena()
        Sena.setupUi(self.IIG5)
        Sena.setNombre(boton.text())
        ruta = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/videos/cuerpo/")
        print(ruta)
        print(os.path.exists(ruta))
        ruta += boton.text() + ".wmv"
        print(os.path.exists(ruta))
        Sena.setPath(ruta)
        Sena.setup(self.IIG5)
        self.IIG5.show()
        #print(boton.text())
    def retranslateUiCuerpo(self,IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_Ojo.setText(_translate("IG4_Aprendizaje", "Ojo"))
        #self.boton_Boca.setText(_translate("IG4_Aprendizaje", "Boca"))
        #self.boton_Brazo.setText(_translate("IG4_Aprendizaje", "Brazo"))
        #self.boton_Codo.setText(_translate("IG4_Aprendizaje", "Codo"))
        self.boton_Cuello.setText(_translate("IG4_Aprendizaje", "Cuello"))
        self.boton_Diente.setText(_translate("IG4_Aprendizaje", "Diente"))
        self.boton_Espalda.setText(_translate("IG4_Aprendizaje", "Espalda"))
        self.boton_Una.setText(_translate("IG4_Aprendizaje", "Uña"))
        #self.boton_Oreja.setText(_translate("IG4_Aprendizaje", "Oreja"))
        self.boton_Estomago.setText(_translate("IG4_Aprendizaje", "Estómago"))
        self.boton_Hombro.setText(_translate("IG4_Aprendizaje", "Hombro"))
        self.boton_Lengua.setText(_translate("IG4_Aprendizaje", "Lengua"))
        self.boton_Mano.setText(_translate("IG4_Aprendizaje", "Mano"))
        self.boton_Muneca.setText(_translate("IG4_Aprendizaje", "Muñeca"))
        self.boton_Nariz.setText(_translate("IG4_Aprendizaje", "Nariz"))
        self.boton_Pulgar.setText(_translate("IG4_Aprendizaje", "Pulgar"))
        self.boton_Pelo.setText(_translate("IG4_Aprendizaje", "Pelo"))

        # Las comentadas son señas dinámicas