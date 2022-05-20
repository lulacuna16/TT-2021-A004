from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
from Clases.Progreso import Progreso
import os


class IG_Dias(object):
    def iniciar_Dias(self,widgetDias):
        self.imagen_Lunes = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Lunes.setGeometry(QtCore.QRect(210, 20, 51, 41))
        self.imagen_Lunes.setObjectName("imagen_Lunes")
        self.boton_Lunes = QtWidgets.QPushButton(widgetDias)
        self.boton_Lunes.setGeometry(QtCore.QRect(200, 70, 75, 31))
        self.boton_Lunes.setStyleSheet("QPushButton{\n"
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
        self.boton_Lunes.setObjectName("boton_Lunes")
        self.imagen_Martes = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Martes.setGeometry(QtCore.QRect(300, 20, 51, 41))
        self.imagen_Martes.setObjectName("imagen_Martes")
        self.boton_Martes = QtWidgets.QPushButton(widgetDias)
        self.boton_Martes.setGeometry(QtCore.QRect(290, 70, 75, 31))
        self.boton_Martes.setStyleSheet("QPushButton{\n"
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
        self.boton_Martes.setObjectName("boton_Martes")
        self.imagen_Miercoles = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Miercoles.setGeometry(QtCore.QRect(390, 20, 51, 41))
        self.imagen_Miercoles.setObjectName("imagen_Miercoles")
        self.boton_Miercoles = QtWidgets.QPushButton(widgetDias)
        self.boton_Miercoles.setGeometry(QtCore.QRect(380, 70, 75, 31))
        self.boton_Miercoles.setStyleSheet("QPushButton{\n"
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
        self.boton_Miercoles.setObjectName("boton_Miercoles")
        self.imagen_Jueves = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Jueves.setGeometry(QtCore.QRect(480, 20, 51, 41))
        self.imagen_Jueves.setObjectName("imagen_Jueves")
        self.boton_Jueves = QtWidgets.QPushButton(widgetDias)
        self.boton_Jueves.setGeometry(QtCore.QRect(470, 70, 75, 31))
        self.boton_Jueves.setStyleSheet("QPushButton{\n"
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
        self.boton_Jueves.setObjectName("boton_Jueves")
        self.imagen_Viernes = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Viernes.setGeometry(QtCore.QRect(570, 20, 51, 41))
        self.imagen_Viernes.setObjectName("imagen_Viernes")
        self.boton_Viernes = QtWidgets.QPushButton(widgetDias)
        self.boton_Viernes.setGeometry(QtCore.QRect(560, 70, 75, 31))
        self.boton_Viernes.setStyleSheet("QPushButton{\n"
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
"}}")
        self.boton_Viernes.setObjectName("boton_Viernes")
        self.imagen_Domingo = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Domingo.setGeometry(QtCore.QRect(430, 120, 51, 41))
        self.imagen_Domingo.setObjectName("imagen_Domingo")
        self.boton_Domingo = QtWidgets.QPushButton(widgetDias)
        self.boton_Domingo.setGeometry(QtCore.QRect(420, 170, 81, 31))
        self.boton_Domingo.setStyleSheet("QPushButton{\n"
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
        self.boton_Domingo.setObjectName("boton_Domingo")
        self.imagen_Sabado = QtWidgets.QGraphicsView(widgetDias)
        self.imagen_Sabado.setGeometry(QtCore.QRect(340, 120, 51, 41))
        self.imagen_Sabado.setObjectName("imagen_Sabado")
        self.boton_Sabado = QtWidgets.QPushButton(widgetDias)
        self.boton_Sabado.setGeometry(QtCore.QRect(330, 170, 75, 31))
        self.boton_Sabado.setStyleSheet("QPushButton{\n"
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
        self.boton_Sabado.setObjectName("boton_Sabado")
        self.label_48 = QtWidgets.QLabel(widgetDias)
        self.label_48.setGeometry(QtCore.QRect(200, 20, 71, 41))
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap("Iconos/lunes.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.label_77 = QtWidgets.QLabel(widgetDias)
        self.label_77.setGeometry(QtCore.QRect(290, 20, 71, 41))
        self.label_77.setText("")
        self.label_77.setPixmap(QtGui.QPixmap("Iconos/martes.png"))
        self.label_77.setScaledContents(True)
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(widgetDias)
        self.label_78.setGeometry(QtCore.QRect(380, 20, 71, 41))
        self.label_78.setText("")
        self.label_78.setPixmap(QtGui.QPixmap("Iconos/miercoles.png"))
        self.label_78.setScaledContents(True)
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(widgetDias)
        self.label_79.setGeometry(QtCore.QRect(470, 20, 71, 41))
        self.label_79.setText("")
        self.label_79.setPixmap(QtGui.QPixmap("Iconos/jueves.png"))
        self.label_79.setScaledContents(True)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(widgetDias)
        self.label_80.setGeometry(QtCore.QRect(560, 20, 71, 41))
        self.label_80.setText("")
        self.label_80.setPixmap(QtGui.QPixmap("Iconos/viernes.png"))
        self.label_80.setScaledContents(True)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(widgetDias)
        self.label_81.setGeometry(QtCore.QRect(330, 120, 71, 41))
        self.label_81.setText("")
        self.label_81.setPixmap(QtGui.QPixmap("Iconos/sabado.png"))
        self.label_81.setScaledContents(True)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(widgetDias)
        self.label_82.setGeometry(QtCore.QRect(420, 120, 81, 41))
        self.label_82.setText("")
        self.label_82.setPixmap(QtGui.QPixmap("Iconos/domingo.png"))
        self.label_82.setScaledContents(True)
        self.label_82.setObjectName("label_82")

        self.pintarVerde()

        self.boton_Domingo.clicked.connect(lambda : self.buttonClicked(self.boton_Domingo))
        self.boton_Lunes.clicked.connect(lambda: self.buttonClicked(self.boton_Lunes))
        self.boton_Martes.clicked.connect(lambda: self.buttonClicked(self.boton_Martes))
        self.boton_Miercoles.clicked.connect(lambda: self.buttonClicked(self.boton_Miercoles))
        self.boton_Jueves.clicked.connect(lambda: self.buttonClicked(self.boton_Jueves))
        self.boton_Viernes.clicked.connect(lambda: self.buttonClicked(self.boton_Viernes))
        self.boton_Sabado.clicked.connect(lambda: self.buttonClicked(self.boton_Sabado))

    def buttonClicked(self, boton):
        self.IG4.hide()
        self.IIG5=QtWidgets.QWidget()
        Sena = IGSena.Ui_IG5_Sena()
        Sena.setIDUsuario(self.id_usuario)
        Sena.setupUi(self.IIG5)
        Sena.setNombre(boton.text())
        ruta = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/videos/dias/")
        print(ruta)
        print(os.path.exists(ruta))
        ruta += boton.text() + ".wmv"
        print(os.path.exists(ruta))
        Sena.setPath(ruta)
        Sena.setup(self.IIG5)
        self.IIG5.show()
        #print(boton.text())

    def retranslateUiDias(self,IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_Lunes.setText(_translate("IG4_Aprendizaje", "Lunes"))
        self.boton_Martes.setText(_translate("IG4_Aprendizaje", "Martes"))
        self.boton_Miercoles.setText(_translate("IG4_Aprendizaje", "Miércoles"))
        self.boton_Jueves.setText(_translate("IG4_Aprendizaje", "Jueves"))
        self.boton_Viernes.setText(_translate("IG4_Aprendizaje", "Viernes"))
        self.boton_Domingo.setText(_translate("IG4_Aprendizaje", "Domingo"))
        self.boton_Sabado.setText(_translate("IG4_Aprendizaje", "Sábado"))

    def setIDUsuario(self,id_usuario):
        self.id_usuario = id_usuario

    def setIG4(self,IG4):
        self.IG4 = IG4

    def pintarVerde(self):
        style = '''QPushButton{\n
                color: rgb(255, 255, 255);\n
                    background-color: rgb(19,207,73);\n
                    font: 12pt \"Segoe Print\";\n
                    border-radius: 11px;\n
                    border:none;\n
                    border-left: 1px solid rgb(18,151,56);\n
                    border-right: 1px solid rgb(18,151,56);\n
                    border-bottom: 3px solid rgb(18,151,56);\n
                }\n
                QPushButton:hover{\n
                    background-color: rgb(43,247,101);\n
                    border-left: 1px solid rgb(18,151,56);\n
                    border-right: 1px solid rgb(18,151,56);\n
                    border-bottom: 3px solid rgb(18,151,56);\n
                }\n
                QPushButton:pressed{\n
                    background-color: rgb(48,182,86);\n
                    border-left: 1px solid rgb(18,151,56);\n
                    border-right: 1px solid rgb(18,151,56);\n
                    border-top: 3px solid rgb(18,151,56);\n
                    border-bottom: none;\n
                }
                '''
        pathBD = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        progreso = Progreso()
        progreso.setBD(pathBD)
        correctas = progreso.senasCorrectasCategoria(self.id_usuario,4) #TRAE LAS SEÑAS (días) YA REALIZADAS POR EL USUARIO (BD)
        print(correctas)
        if "lunes" in correctas:
            self.boton_Lunes.setStyleSheet(style)
        if "martes" in correctas:
            self.boton_Martes.setStyleSheet(style)
        if "miercoles" in correctas:
            self.boton_Miercoles.setStyleSheet(style)
        if "jueves" in correctas:
            self.boton_Jueves.setStyleSheet(style)
        if "viernes" in correctas:
            self.boton_Viernes.setStyleSheet(style)
        if "sabado" in correctas:
            self.boton_Sabado.setStyleSheet(style)
        if "domingo" in correctas:
            self.boton_Domingo.setStyleSheet(style)