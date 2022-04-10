from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
from Clases.Progreso import Progreso
import os


class IG_Colores(object):
    def iniciar_Colores(self,widgetColores):
        self.imagen_Amarillo = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Amarillo.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.imagen_Amarillo.setObjectName("imagen_Amarillo")
        self.boton_Amarillo = QtWidgets.QPushButton(widgetColores)
        self.boton_Amarillo.setGeometry(QtCore.QRect(210, 70, 75, 31))
        self.boton_Amarillo.setStyleSheet("QPushButton{\n"
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
        self.boton_Amarillo.setObjectName("boton_Amarillo")
        self.imagen_Azul = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Azul.setGeometry(QtCore.QRect(310, 20, 51, 41))
        self.imagen_Azul.setObjectName("imagen_Azul")
        self.boton_Azul = QtWidgets.QPushButton(widgetColores)
        self.boton_Azul.setGeometry(QtCore.QRect(300, 70, 75, 31))
        self.boton_Azul.setStyleSheet("QPushButton{\n"
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
        self.boton_Azul.setObjectName("boton_Azul")
        self.imagen_Blanco = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Blanco.setGeometry(QtCore.QRect(400, 20, 51, 41))
        self.imagen_Blanco.setObjectName("imagen_Blanco")
        self.boton_Blanco = QtWidgets.QPushButton(widgetColores)
        self.boton_Blanco.setGeometry(QtCore.QRect(390, 70, 75, 31))
        self.boton_Blanco.setStyleSheet("QPushButton{\n"
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
        self.boton_Blanco.setObjectName("boton_Blanco")
        self.imagen_Cafe = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Cafe.setGeometry(QtCore.QRect(490, 20, 51, 41))
        self.imagen_Cafe.setObjectName("imagen_Cafe")
        self.boton_Cafe = QtWidgets.QPushButton(widgetColores)
        self.boton_Cafe.setGeometry(QtCore.QRect(480, 70, 75, 31))
        self.boton_Cafe.setStyleSheet("QPushButton{\n"
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
        self.boton_Cafe.setObjectName("boton_Cafe")
        self.imagen_Rojo = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Rojo.setGeometry(QtCore.QRect(270, 220, 51, 41))
        self.imagen_Rojo.setObjectName("imagen_Rojo")
        self.boton_Rojo = QtWidgets.QPushButton(widgetColores)
        self.boton_Rojo.setGeometry(QtCore.QRect(260, 270, 75, 23))
        self.boton_Rojo.setStyleSheet("QPushButton{\n"
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
        self.boton_Rojo.setObjectName("boton_Rojo")
        self.imagen_Gris = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Gris.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_Gris.setObjectName("imagen_Gris")
        self.boton_Gris = QtWidgets.QPushButton(widgetColores)
        self.boton_Gris.setGeometry(QtCore.QRect(210, 170, 75, 31))
        self.boton_Gris.setStyleSheet("QPushButton{\n"
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
        self.boton_Gris.setObjectName("boton_Gris")
        self.imagen_Morado = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Morado.setGeometry(QtCore.QRect(310, 120, 51, 41))
        self.imagen_Morado.setObjectName("imagen_Morado")
        self.boton_Morado = QtWidgets.QPushButton(widgetColores)
        self.boton_Morado.setGeometry(QtCore.QRect(300, 170, 75, 31))
        self.boton_Morado.setStyleSheet("QPushButton{\n"
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
        self.boton_Morado.setObjectName("boton_Morado")
        self.imagen_Naranja = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Naranja.setGeometry(QtCore.QRect(400, 120, 51, 41))
        self.imagen_Naranja.setObjectName("imagen_Naranja")
        self.boton_Naranja = QtWidgets.QPushButton(widgetColores)
        self.boton_Naranja.setGeometry(QtCore.QRect(390, 170, 75, 31))
        self.boton_Naranja.setStyleSheet("QPushButton{\n"
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
        self.boton_Naranja.setObjectName("boton_Naranja")
        self.imagen_Negro = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Negro.setGeometry(QtCore.QRect(490, 120, 51, 41))
        self.imagen_Negro.setObjectName("imagen_Negro")
        self.boton_Negro = QtWidgets.QPushButton(widgetColores)
        self.boton_Negro.setGeometry(QtCore.QRect(480, 170, 75, 31))
        self.boton_Negro.setStyleSheet("QPushButton{\n"
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
        self.boton_Negro.setObjectName("boton_Negro")
        self.imagen_Verde = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Verde.setGeometry(QtCore.QRect(450, 220, 51, 41))
        self.imagen_Verde.setObjectName("imagen_Verde")
        self.boton_Verde = QtWidgets.QPushButton(widgetColores)
        self.boton_Verde.setGeometry(QtCore.QRect(440, 270, 75, 23))
        self.boton_Verde.setStyleSheet("QPushButton{\n"
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
        self.boton_Verde.setObjectName("boton_Verde")
        self.imagen_Rosa = QtWidgets.QGraphicsView(widgetColores)
        self.imagen_Rosa.setGeometry(QtCore.QRect(360, 220, 51, 41))
        self.imagen_Rosa.setObjectName("imagen_Rosa")
        self.boton_Rosa = QtWidgets.QPushButton(widgetColores)
        self.boton_Rosa.setGeometry(QtCore.QRect(350, 270, 75, 23))
        self.boton_Rosa.setStyleSheet("QPushButton{\n"
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
        self.boton_Rosa.setObjectName("boton_Rosa")
        self.label_66 = QtWidgets.QLabel(widgetColores)
        self.label_66.setGeometry(QtCore.QRect(210, -20, 71, 81))
        self.label_66.setText("")
        self.label_66.setPixmap(QtGui.QPixmap("Iconos/amarillo.png"))
        self.label_66.setScaledContents(True)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(widgetColores)
        self.label_67.setGeometry(QtCore.QRect(300, -20, 71, 81))
        self.label_67.setText("")
        self.label_67.setPixmap(QtGui.QPixmap("Iconos/azul.png"))
        self.label_67.setScaledContents(True)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(widgetColores)
        self.label_68.setGeometry(QtCore.QRect(270, 220, 61, 41))
        self.label_68.setText("")
        self.label_68.setPixmap(QtGui.QPixmap("Iconos/rojo.png"))
        self.label_68.setScaledContents(True)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(widgetColores)
        self.label_69.setGeometry(QtCore.QRect(450, 220, 61, 41))
        self.label_69.setText("")
        self.label_69.setPixmap(QtGui.QPixmap("Iconos/verde.png"))
        self.label_69.setScaledContents(True)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(widgetColores)
        self.label_70.setGeometry(QtCore.QRect(360, 220, 61, 41))
        self.label_70.setText("")
        self.label_70.setPixmap(QtGui.QPixmap("Iconos/rosa.png"))
        self.label_70.setScaledContents(True)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(widgetColores)
        self.label_71.setGeometry(QtCore.QRect(490, 20, 61, 41))
        self.label_71.setText("")
        self.label_71.setPixmap(QtGui.QPixmap("Iconos/café.png"))
        self.label_71.setScaledContents(True)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(widgetColores)
        self.label_72.setGeometry(QtCore.QRect(220, 120, 61, 41))
        self.label_72.setText("")
        self.label_72.setPixmap(QtGui.QPixmap("Iconos/gris.png"))
        self.label_72.setScaledContents(True)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(widgetColores)
        self.label_73.setGeometry(QtCore.QRect(310, 120, 61, 41))
        self.label_73.setText("")
        self.label_73.setPixmap(QtGui.QPixmap("Iconos/morado.png"))
        self.label_73.setScaledContents(True)
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(widgetColores)
        self.label_74.setGeometry(QtCore.QRect(400, 120, 61, 41))
        self.label_74.setText("")
        self.label_74.setPixmap(QtGui.QPixmap("Iconos/naranja.png"))
        self.label_74.setScaledContents(True)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(widgetColores)
        self.label_75.setGeometry(QtCore.QRect(490, 120, 61, 41))
        self.label_75.setText("")
        self.label_75.setPixmap(QtGui.QPixmap("Iconos/negro.png"))
        self.label_75.setScaledContents(True)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(widgetColores)
        self.label_76.setGeometry(QtCore.QRect(400, 20, 61, 41))
        self.label_76.setText("")
        self.label_76.setPixmap(QtGui.QPixmap("Iconos/blanco.png"))
        self.label_76.setScaledContents(True)
        self.label_76.setObjectName("label_76")

        self.pintarVerde()

        self.boton_Amarillo.clicked.connect(lambda: self.buttonClicked(self.boton_Amarillo))
        self.boton_Azul.clicked.connect(lambda: self.buttonClicked(self.boton_Azul))
        self.boton_Blanco.clicked.connect(lambda: self.buttonClicked(self.boton_Blanco))
        self.boton_Cafe.clicked.connect(lambda: self.buttonClicked(self.boton_Cafe))
        self.boton_Gris.clicked.connect(lambda: self.buttonClicked(self.boton_Gris))
        self.boton_Morado.clicked.connect(lambda: self.buttonClicked(self.boton_Morado))
        self.boton_Naranja.clicked.connect(lambda: self.buttonClicked(self.boton_Naranja))
        self.boton_Negro.clicked.connect(lambda: self.buttonClicked(self.boton_Negro))
        self.boton_Rojo.clicked.connect(lambda: self.buttonClicked(self.boton_Rojo))
        self.boton_Rosa.clicked.connect(lambda: self.buttonClicked(self.boton_Rosa))
        self.boton_Verde.clicked.connect(lambda: self.buttonClicked(self.boton_Verde))

    def buttonClicked(self, boton):
        self.IIG5=QtWidgets.QWidget()
        Sena = IGSena.Ui_IG5_Sena()
        Sena.setIDUsuario(self.id_usuario)
        Sena.setupUi(self.IIG5)
        Sena.setNombre(boton.text())
        ruta = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/videos/colores/")
        print(ruta)
        print(os.path.exists(ruta))
        ruta += boton.text() + ".wmv"
        print(os.path.exists(ruta))
        Sena.setPath(ruta)
        Sena.setup(self.IIG5)
        self.IIG5.show()
        #print(boton.text())

    def retranslateUiColores(self,IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_Amarillo.setText(_translate("IG4_Aprendizaje", "Amarillo"))
        self.boton_Azul.setText(_translate("IG4_Aprendizaje", "Azul"))
        self.boton_Blanco.setText(_translate("IG4_Aprendizaje", "Blanco"))
        self.boton_Cafe.setText(_translate("IG4_Aprendizaje", "Café"))
        self.boton_Rojo.setText(_translate("IG4_Aprendizaje", "Rojo"))
        self.boton_Gris.setText(_translate("IG4_Aprendizaje", "Gris"))
        self.boton_Morado.setText(_translate("IG4_Aprendizaje", "Morado"))
        self.boton_Naranja.setText(_translate("IG4_Aprendizaje", "Naranja"))
        self.boton_Negro.setText(_translate("IG4_Aprendizaje", "Negro"))
        self.boton_Verde.setText(_translate("IG4_Aprendizaje", "Verde"))
        self.boton_Rosa.setText(_translate("IG4_Aprendizaje", "Rosa"))

    def setIDUsuario(self,id_usuario):
        self.id_usuario = id_usuario

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
        correctas = progreso.senasCorrectasCategoria(self.id_usuario,5) #TRAE LAS SEÑAS (colores) YA REALIZADAS POR EL USUARIO (BD)
        print(correctas)
        if "amarillo" in correctas:
            self.boton_Amarillo.setStyleSheet(style)
        if "azul" in correctas:
            self.boton_Azul.setStyleSheet(style)
        if "blanco" in correctas:
            self.boton_Blanco.setStyleSheet(style)
        if "cafe" in correctas:
            self.boton_Cafe.setStyleSheet(style)
        if "gris" in correctas:
            self.boton_Gris.setStyleSheet(style)
        if "morado" in correctas:
            self.boton_Morado.setStyleSheet(style)
        if "naranja" in correctas:
            self.boton_Naranja.setStyleSheet(style)
        if "negro" in correctas:
            self.boton_Negro.setStyleSheet(style)
        if "rojo" in correctas:
            self.boton_Rojo.setStyleSheet(style)
        if "rosa" in correctas:
            self.boton_Rosa.setStyleSheet(style)
        if "verde" in correctas:
            self.boton_Verde.setStyleSheet(style)