from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
import os

class IG_Cuerpo(object):
    def iniciar_Cuerpo(self, widgetCuerpo):
        self.imagen_Ojo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Ojo.setGeometry(QtCore.QRect(180, 220, 51, 41))
        self.imagen_Ojo.setObjectName("imagen_Ojo")
        self.boton_Ojo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Ojo.setGeometry(QtCore.QRect(170, 270, 75, 31))
        self.boton_Ojo.setStyleSheet("QPushButton{\n"
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
        self.boton_Ojo.setObjectName("boton_Ojo")
        self.imagen_Boca = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Boca.setGeometry(QtCore.QRect(130, 20, 51, 41))
        self.imagen_Boca.setObjectName("imagen_Boca")
        self.boton_Boca = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Boca.setGeometry(QtCore.QRect(120, 70, 75, 31))
        self.boton_Boca.setStyleSheet("QPushButton{\n"
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
        self.boton_Boca.setObjectName("boton_Boca")
        self.imagen_Brazo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Brazo.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.imagen_Brazo.setObjectName("imagen_Brazo")
        self.boton_Brazo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Brazo.setGeometry(QtCore.QRect(210, 70, 75, 31))
        self.boton_Brazo.setStyleSheet("QPushButton{\n"
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
        self.boton_Brazo.setObjectName("boton_Brazo")
        self.imagen_Codo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Codo.setGeometry(QtCore.QRect(310, 20, 51, 41))
        self.imagen_Codo.setObjectName("imagen_Codo")
        self.boton_Codo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Codo.setGeometry(QtCore.QRect(300, 70, 75, 31))
        self.boton_Codo.setStyleSheet("QPushButton{\n"
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
        self.boton_Codo.setObjectName("boton_Codo")
        self.imagen_Cuello = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Cuello.setGeometry(QtCore.QRect(400, 20, 51, 41))
        self.imagen_Cuello.setObjectName("imagen_Cuello")
        self.boton_Cuello = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Cuello.setGeometry(QtCore.QRect(390, 70, 75, 31))
        self.boton_Cuello.setStyleSheet("QPushButton{\n"
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
        self.boton_Cuello.setObjectName("boton_Cuello")
        self.imagen_Diente = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Diente.setGeometry(QtCore.QRect(490, 20, 51, 41))
        self.imagen_Diente.setObjectName("imagen_Diente")
        self.boton_Diente = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Diente.setGeometry(QtCore.QRect(480, 70, 75, 31))
        self.boton_Diente.setStyleSheet("QPushButton{\n"
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
        self.boton_Diente.setObjectName("boton_Diente")
        self.imagen_Espalda = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Espalda.setGeometry(QtCore.QRect(580, 20, 51, 41))
        self.imagen_Espalda.setObjectName("imagen_Espalda")
        self.boton_Espalda = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Espalda.setGeometry(QtCore.QRect(570, 70, 75, 31))
        self.boton_Espalda.setStyleSheet("QPushButton{\n"
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
        self.boton_Espalda.setObjectName("boton_Espalda")
        self.imagen_Una = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Una.setGeometry(QtCore.QRect(540, 220, 51, 41))
        self.imagen_Una.setObjectName("imagen_Una")
        self.boton_Una = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Una.setGeometry(QtCore.QRect(530, 270, 75, 31))
        self.boton_Una.setStyleSheet("QPushButton{\n"
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
        self.boton_Una.setObjectName("boton_Una")
        self.imagen_Oreja = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Oreja.setGeometry(QtCore.QRect(270, 220, 51, 41))
        self.imagen_Oreja.setObjectName("imagen_Oreja")
        self.boton_Oreja = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Oreja.setGeometry(QtCore.QRect(260, 270, 75, 31))
        self.boton_Oreja.setStyleSheet("QPushButton{\n"
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
        self.boton_Oreja.setObjectName("boton_Oreja")
        self.imagen_Estomago = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Estomago.setGeometry(QtCore.QRect(130, 120, 51, 41))
        self.imagen_Estomago.setObjectName("imagen_Estomago")
        self.boton_Estomago = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Estomago.setGeometry(QtCore.QRect(114, 170, 81, 31))
        self.boton_Estomago.setStyleSheet("QPushButton{\n"
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
        self.boton_Estomago.setObjectName("boton_Estomago")
        self.imagen_Hombro = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Hombro.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_Hombro.setObjectName("imagen_Hombro")
        self.boton_Hombro = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Hombro.setGeometry(QtCore.QRect(210, 170, 75, 31))
        self.boton_Hombro.setStyleSheet("QPushButton{\n"
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
        self.boton_Hombro.setObjectName("boton_Hombro")
        self.imagen_Lengua = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Lengua.setGeometry(QtCore.QRect(310, 120, 51, 41))
        self.imagen_Lengua.setObjectName("imagen_Lengua")
        self.boton_Lengua = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Lengua.setGeometry(QtCore.QRect(300, 170, 75, 31))
        self.boton_Lengua.setStyleSheet("QPushButton{\n"
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
        self.boton_Lengua.setObjectName("boton_Lengua")
        self.imagen_Mano = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Mano.setGeometry(QtCore.QRect(400, 120, 51, 41))
        self.imagen_Mano.setObjectName("imagen_Mano")
        self.boton_Mano = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Mano.setGeometry(QtCore.QRect(390, 170, 75, 31))
        self.boton_Mano.setStyleSheet("QPushButton{\n"
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
        self.boton_Mano.setObjectName("boton_Mano")
        self.imagen_Muneca = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Muneca.setGeometry(QtCore.QRect(490, 120, 51, 41))
        self.imagen_Muneca.setObjectName("imagen_Muneca")
        self.boton_Muneca = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Muneca.setGeometry(QtCore.QRect(480, 170, 75, 31))
        self.boton_Muneca.setStyleSheet("QPushButton{\n"
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
        self.boton_Muneca.setObjectName("boton_Muneca")
        self.imagen_Nariz = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Nariz.setGeometry(QtCore.QRect(580, 120, 51, 41))
        self.imagen_Nariz.setObjectName("imagen_Nariz")
        self.boton_Nariz = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Nariz.setGeometry(QtCore.QRect(570, 170, 75, 31))
        self.boton_Nariz.setStyleSheet("QPushButton{\n"
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
        self.boton_Nariz.setObjectName("boton_Nariz")
        self.imagen_Pulgar = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Pulgar.setGeometry(QtCore.QRect(450, 220, 51, 41))
        self.imagen_Pulgar.setObjectName("imagen_Pulgar")
        self.boton_Pulgar = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Pulgar.setGeometry(QtCore.QRect(440, 270, 75, 31))
        self.boton_Pulgar.setStyleSheet("QPushButton{\n"
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
        self.boton_Pulgar.setObjectName("boton_Pulgar")
        self.imagen_Pelo = QtWidgets.QGraphicsView(widgetCuerpo)
        self.imagen_Pelo.setGeometry(QtCore.QRect(360, 220, 51, 41))
        self.imagen_Pelo.setObjectName("imagen_Pelo")
        self.boton_Pelo = QtWidgets.QPushButton(widgetCuerpo)
        self.boton_Pelo.setGeometry(QtCore.QRect(350, 270, 75, 31))
        self.boton_Pelo.setStyleSheet("QPushButton{\n"
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
        self.boton_Pelo.setObjectName("boton_Pelo")
        self.label_49 = QtWidgets.QLabel(widgetCuerpo)
        self.label_49.setGeometry(QtCore.QRect(210, 20, 71, 41))
        self.label_49.setText("")
        self.label_49.setPixmap(QtGui.QPixmap("Iconos/brazo.png"))
        self.label_49.setScaledContents(True)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(widgetCuerpo)
        self.label_50.setGeometry(QtCore.QRect(390, 120, 71, 41))
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap("Iconos/mano.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setObjectName("label_50")
        self.label_52 = QtWidgets.QLabel(widgetCuerpo)
        self.label_52.setGeometry(QtCore.QRect(300, 10, 71, 51))
        self.label_52.setText("")
        self.label_52.setPixmap(QtGui.QPixmap("Iconos/codo.png"))
        self.label_52.setScaledContents(True)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(widgetCuerpo)
        self.label_53.setGeometry(QtCore.QRect(480, 10, 81, 51))
        self.label_53.setText("")
        self.label_53.setPixmap(QtGui.QPixmap("Iconos/diente.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(widgetCuerpo)
        self.label_54.setGeometry(QtCore.QRect(390, -50, 71, 111))
        self.label_54.setText("")
        self.label_54.setPixmap(QtGui.QPixmap("Iconos/cuello.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(widgetCuerpo)
        self.label_55.setGeometry(QtCore.QRect(570, 10, 71, 51))
        self.label_55.setText("")
        self.label_55.setPixmap(QtGui.QPixmap("Iconos/espalda.png"))
        self.label_55.setScaledContents(True)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(widgetCuerpo)
        self.label_56.setGeometry(QtCore.QRect(120, 100, 71, 61))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap("Iconos/estomago.png"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(widgetCuerpo)
        self.label_57.setGeometry(QtCore.QRect(210, 100, 71, 61))
        self.label_57.setText("")
        self.label_57.setPixmap(QtGui.QPixmap("Iconos/hombro.png"))
        self.label_57.setScaledContents(True)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(widgetCuerpo)
        self.label_58.setGeometry(QtCore.QRect(300, 100, 81, 61))
        self.label_58.setText("")
        self.label_58.setPixmap(QtGui.QPixmap("Iconos/lengua.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(widgetCuerpo)
        self.label_59.setGeometry(QtCore.QRect(480, 100, 81, 61))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("Iconos/muñeca.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(widgetCuerpo)
        self.label_60.setGeometry(QtCore.QRect(570, 110, 81, 51))
        self.label_60.setText("")
        self.label_60.setPixmap(QtGui.QPixmap("Iconos/nariz.png"))
        self.label_60.setScaledContents(True)
        self.label_60.setObjectName("label_60")
        self.label_63 = QtWidgets.QLabel(widgetCuerpo)
        self.label_63.setGeometry(QtCore.QRect(350, 220, 81, 41))
        self.label_63.setText("")
        self.label_63.setPixmap(QtGui.QPixmap("Iconos/pelo.png"))
        self.label_63.setScaledContents(True)
        self.label_63.setObjectName("label_63")
        self.label_61 = QtWidgets.QLabel(widgetCuerpo)
        self.label_61.setGeometry(QtCore.QRect(170, 220, 81, 41))
        self.label_61.setText("")
        self.label_61.setPixmap(QtGui.QPixmap("Iconos/ojo.png"))
        self.label_61.setScaledContents(True)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(widgetCuerpo)
        self.label_62.setGeometry(QtCore.QRect(440, 220, 81, 41))
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap("Iconos/pulgar.png"))
        self.label_62.setScaledContents(True)
        self.label_62.setObjectName("label_62")
        self.label_64 = QtWidgets.QLabel(widgetCuerpo)
        self.label_64.setGeometry(QtCore.QRect(530, 220, 81, 41))
        self.label_64.setText("")
        self.label_64.setPixmap(QtGui.QPixmap("Iconos/uña.png"))
        self.label_64.setScaledContents(True)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(widgetCuerpo)
        self.label_65.setGeometry(QtCore.QRect(260, 220, 81, 41))
        self.label_65.setText("")
        self.label_65.setPixmap(QtGui.QPixmap("Iconos/oreja.png"))
        self.label_65.setScaledContents(True)
        self.label_65.setObjectName("label_65")
        self.label_51 = QtWidgets.QLabel(widgetCuerpo)
        self.label_51.setGeometry(QtCore.QRect(120, -20, 71, 81))
        self.label_51.setText("")
        self.label_51.setPixmap(QtGui.QPixmap("Iconos/boca.png"))
        self.label_51.setScaledContents(True)
        self.label_51.setObjectName("label_51")

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
        self.boton_Boca.setText(_translate("IG4_Aprendizaje", "Boca"))
        self.boton_Brazo.setText(_translate("IG4_Aprendizaje", "Brazo"))
        self.boton_Codo.setText(_translate("IG4_Aprendizaje", "Codo"))
        self.boton_Cuello.setText(_translate("IG4_Aprendizaje", "Cuello"))
        self.boton_Diente.setText(_translate("IG4_Aprendizaje", "Diente"))
        self.boton_Espalda.setText(_translate("IG4_Aprendizaje", "Espalda"))
        self.boton_Una.setText(_translate("IG4_Aprendizaje", "Uña"))
        self.boton_Oreja.setText(_translate("IG4_Aprendizaje", "Oreja"))
        self.boton_Estomago.setText(_translate("IG4_Aprendizaje", "Estómago"))
        self.boton_Hombro.setText(_translate("IG4_Aprendizaje", "Hombro"))
        self.boton_Lengua.setText(_translate("IG4_Aprendizaje", "Lengua"))
        self.boton_Mano.setText(_translate("IG4_Aprendizaje", "Mano"))
        self.boton_Muneca.setText(_translate("IG4_Aprendizaje", "Muñeca"))
        self.boton_Nariz.setText(_translate("IG4_Aprendizaje", "Nariz"))
        self.boton_Pulgar.setText(_translate("IG4_Aprendizaje", "Pulgar"))
        self.boton_Pelo.setText(_translate("IG4_Aprendizaje", "Pelo"))

        # Las comentadas son señas dinámicas