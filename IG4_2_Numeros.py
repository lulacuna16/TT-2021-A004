from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
import os
NumerosEstaticos=["1","2","3","4","5","6","7","8"]
class IG_Numeros(object):
    def iniciar_Numeros(self,widgetNumeros):
        self.imagen_1 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_1.setGeometry(QtCore.QRect(40, 20, 51, 41))
        self.imagen_1.setObjectName("imagen_1")
        self.boton_1 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_1.setGeometry(QtCore.QRect(30, 70, 75, 31))
        self.boton_1.setStyleSheet("QPushButton{\n"
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
        self.boton_1.setObjectName("boton_1")
        self.imagen_2 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_2.setGeometry(QtCore.QRect(130, 20, 51, 41))
        self.imagen_2.setObjectName("imagen_2")
        self.boton_2 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_2.setGeometry(QtCore.QRect(120, 70, 75, 31))
        self.boton_2.setStyleSheet("QPushButton{\n"
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
        self.boton_2.setObjectName("boton_2")
        self.imagen_3 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_3.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.imagen_3.setObjectName("imagen_3")
        self.boton_3 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_3.setGeometry(QtCore.QRect(210, 70, 75, 31))
        self.boton_3.setStyleSheet("QPushButton{\n"
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
        self.boton_3.setObjectName("boton_3")
        self.imagen_4 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_4.setGeometry(QtCore.QRect(310, 20, 51, 41))
        self.imagen_4.setObjectName("imagen_4")
        self.boton_4 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_4.setGeometry(QtCore.QRect(300, 70, 75, 31))
        self.boton_4.setStyleSheet("QPushButton{\n"
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
        self.boton_4.setObjectName("boton_4")
        self.imagen_5 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_5.setGeometry(QtCore.QRect(400, 20, 51, 41))
        self.imagen_5.setObjectName("imagen_5")
        self.boton_5 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_5.setGeometry(QtCore.QRect(390, 70, 75, 31))
        self.boton_5.setStyleSheet("QPushButton{\n"
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
        self.boton_5.setObjectName("boton_5")
        self.imagen_6 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_6.setGeometry(QtCore.QRect(490, 20, 51, 41))
        self.imagen_6.setObjectName("imagen_6")
        self.boton_6 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_6.setGeometry(QtCore.QRect(480, 70, 75, 31))
        self.boton_6.setStyleSheet("QPushButton{\n"
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
        self.boton_6.setObjectName("boton_6")
        self.imagen_7 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_7.setGeometry(QtCore.QRect(580, 20, 51, 41))
        self.imagen_7.setObjectName("imagen_7")
        self.boton_7 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_7.setGeometry(QtCore.QRect(570, 70, 75, 31))
        self.boton_7.setStyleSheet("QPushButton{\n"
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
        self.boton_7.setObjectName("boton_7")
        self.imagen_8 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_8.setGeometry(QtCore.QRect(670, 20, 51, 41))
        self.imagen_8.setObjectName("imagen_8")
        self.boton_8 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_8.setGeometry(QtCore.QRect(660, 70, 75, 31))
        self.boton_8.setStyleSheet("QPushButton{\n"
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
        self.boton_8.setObjectName("boton_8")
        self.imagen_9 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_9.setGeometry(QtCore.QRect(760, 20, 51, 41))
        self.imagen_9.setObjectName("imagen_9")
        self.boton_9 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_9.setGeometry(QtCore.QRect(750, 70, 75, 31))
        self.boton_9.setStyleSheet("QPushButton{\n"
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
        self.boton_9.setObjectName("boton_9")
        self.imagen_10 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_10.setGeometry(QtCore.QRect(40, 120, 51, 41))
        self.imagen_10.setObjectName("imagen_10")
        self.boton_10 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_10.setGeometry(QtCore.QRect(30, 170, 75, 31))
        self.boton_10.setStyleSheet("QPushButton{\n"
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
        self.boton_10.setObjectName("boton_10")
        self.imagen_20 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_20.setGeometry(QtCore.QRect(130, 120, 51, 41))
        self.imagen_20.setObjectName("imagen_20")
        self.boton_20 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_20.setGeometry(QtCore.QRect(120, 170, 75, 31))
        self.boton_20.setStyleSheet("QPushButton{\n"
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
        self.boton_20.setObjectName("boton_20")
        self.imagen_30 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_30.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_30.setObjectName("imagen_30")
        self.boton_30 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_30.setGeometry(QtCore.QRect(210, 170, 75, 31))
        self.boton_30.setStyleSheet("QPushButton{\n"
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
        self.boton_30.setObjectName("boton_30")
        self.imagen_40 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_40.setGeometry(QtCore.QRect(310, 120, 51, 41))
        self.imagen_40.setObjectName("imagen_40")
        self.boton_40 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_40.setGeometry(QtCore.QRect(300, 170, 75, 31))
        self.boton_40.setStyleSheet("QPushButton{\n"
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
        self.boton_40.setObjectName("boton_40")
        self.imagen_50 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_50.setGeometry(QtCore.QRect(400, 120, 51, 41))
        self.imagen_50.setObjectName("imagen_50")
        self.boton_50 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_50.setGeometry(QtCore.QRect(390, 170, 75, 31))
        self.boton_50.setStyleSheet("QPushButton{\n"
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
        self.boton_50.setObjectName("boton_50")
        self.imagen_60 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_60.setGeometry(QtCore.QRect(490, 120, 51, 41))
        self.imagen_60.setObjectName("imagen_60")
        self.boton_60 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_60.setGeometry(QtCore.QRect(480, 170, 75, 31))
        self.boton_60.setStyleSheet("QPushButton{\n"
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
        self.boton_60.setObjectName("boton_60")
        self.imagen_70 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_70.setGeometry(QtCore.QRect(580, 120, 51, 41))
        self.imagen_70.setObjectName("imagen_70")
        self.boton_70 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_70.setGeometry(QtCore.QRect(570, 170, 75, 31))
        self.boton_70.setStyleSheet("QPushButton{\n"
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
        self.boton_70.setObjectName("boton_70")
        self.imagen_80 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_80.setGeometry(QtCore.QRect(670, 120, 51, 41))
        self.imagen_80.setObjectName("imagen_80")
        self.boton_80 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_80.setGeometry(QtCore.QRect(660, 170, 75, 31))
        self.boton_80.setStyleSheet("QPushButton{\n"
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
        self.boton_80.setObjectName("boton_80")
        self.imagen_90 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_90.setGeometry(QtCore.QRect(760, 120, 51, 41))
        self.imagen_90.setObjectName("imagen_90")
        self.boton_90 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_90.setGeometry(QtCore.QRect(750, 170, 75, 31))
        self.boton_90.setStyleSheet("QPushButton{\n"
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
        self.boton_90.setObjectName("boton_90")
        self.imagen_100 = QtWidgets.QGraphicsView(widgetNumeros)
        self.imagen_100.setGeometry(QtCore.QRect(410, 220, 51, 41))
        self.imagen_100.setObjectName("imagen_100")
        self.boton_100 = QtWidgets.QPushButton(widgetNumeros)
        self.boton_100.setGeometry(QtCore.QRect(390, 270, 75, 31))
        self.boton_100.setStyleSheet("QPushButton{\n"
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
        self.boton_100.setObjectName("boton_100")
        self.label_28 = QtWidgets.QLabel(widgetNumeros)
        self.label_28.setGeometry(QtCore.QRect(40, 10, 51, 51))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("Iconos/1.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(widgetNumeros)
        self.label_29.setGeometry(QtCore.QRect(130, 10, 51, 51))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("Iconos/2.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(widgetNumeros)
        self.label_30.setGeometry(QtCore.QRect(220, 10, 51, 51))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("Iconos/3.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(widgetNumeros)
        self.label_31.setGeometry(QtCore.QRect(310, 10, 51, 51))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("Iconos/4.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(widgetNumeros)
        self.label_32.setGeometry(QtCore.QRect(400, 10, 51, 51))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("Iconos/5.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(widgetNumeros)
        self.label_33.setGeometry(QtCore.QRect(490, 10, 51, 51))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("Iconos/6.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(widgetNumeros)
        self.label_34.setGeometry(QtCore.QRect(580, 10, 51, 51))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("Iconos/7.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(widgetNumeros)
        self.label_35.setGeometry(QtCore.QRect(670, 10, 51, 51))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("Iconos/8.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(widgetNumeros)
        self.label_36.setGeometry(QtCore.QRect(760, 10, 51, 51))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("Iconos/9.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.label_38 = QtWidgets.QLabel(widgetNumeros)
        self.label_38.setGeometry(QtCore.QRect(30, 110, 71, 51))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("Iconos/10.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(widgetNumeros)
        self.label_39.setGeometry(QtCore.QRect(120, 110, 71, 51))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("Iconos/20.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(widgetNumeros)
        self.label_40.setGeometry(QtCore.QRect(210, 110, 71, 51))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("Iconos/30.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(widgetNumeros)
        self.label_41.setGeometry(QtCore.QRect(300, 110, 71, 51))
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap("Iconos/40.png"))
        self.label_41.setScaledContents(True)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(widgetNumeros)
        self.label_42.setGeometry(QtCore.QRect(390, 110, 71, 51))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("Iconos/50.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(widgetNumeros)
        self.label_43.setGeometry(QtCore.QRect(480, 110, 71, 51))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("Iconos/60.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(widgetNumeros)
        self.label_44.setGeometry(QtCore.QRect(570, 110, 71, 51))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("Iconos/70.png"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(widgetNumeros)
        self.label_45.setGeometry(QtCore.QRect(660, 110, 71, 51))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("Iconos/80.png"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(widgetNumeros)
        self.label_46.setGeometry(QtCore.QRect(750, 110, 71, 51))
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap("Iconos/90.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(widgetNumeros)
        self.label_47.setGeometry(QtCore.QRect(390, 210, 81, 51))
        self.label_47.setText("")
        self.label_47.setPixmap(QtGui.QPixmap("Iconos/100.png"))
        self.label_47.setScaledContents(True)
        self.label_47.setObjectName("label_47")
        self.boton_1.clicked.connect(lambda: self.buttonClicked(self.boton_1))
        self.boton_2.clicked.connect(lambda: self.buttonClicked(self.boton_2))
        self.boton_3.clicked.connect(lambda: self.buttonClicked(self.boton_3))
        self.boton_4.clicked.connect(lambda: self.buttonClicked(self.boton_4))
        self.boton_5.clicked.connect(lambda: self.buttonClicked(self.boton_5))
        self.boton_6.clicked.connect(lambda: self.buttonClicked(self.boton_6))
        self.boton_7.clicked.connect(lambda: self.buttonClicked(self.boton_7))
        self.boton_8.clicked.connect(lambda: self.buttonClicked(self.boton_8))

        """self.boton_9.clicked.connect(lambda: self.buttonClicked(self.boton_9))
        self.boton_10.clicked.connect(lambda: self.buttonClicked(self.boton_10))
        self.boton_20.clicked.connect(lambda: self.buttonClicked(self.boton_20))
        self.boton_30.clicked.connect(lambda: self.buttonClicked(self.boton_30))
        self.boton_40.clicked.connect(lambda: self.buttonClicked(self.boton_40))
        self.boton_50.clicked.connect(lambda: self.buttonClicked(self.boton_50))
        self.boton_60.clicked.connect(lambda: self.buttonClicked(self.boton_60))
        self.boton_70.clicked.connect(lambda: self.buttonClicked(self.boton_70))
        self.boton_80.clicked.connect(lambda: self.buttonClicked(self.boton_80))
        self.boton_90.clicked.connect(lambda: self.buttonClicked(self.boton_90))
        self.boton_100.clicked.connect(lambda: self.buttonClicked(self.boton_100))
        """
    def buttonClicked(self, boton):
        self.IIG5=QtWidgets.QWidget()
        Sena = IGSena.Ui_IG5_Sena()
        Sena.setupUi(self.IIG5)
        Sena.setNombre(boton.text())
        ruta = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/videos/numeros/")
        #print(ruta)
        #print(os.path.exists(ruta))
        ruta += boton.text() + ".wmv"
        #print(os.path.exists(ruta))
        Sena.setPath(ruta)
        if boton.text() in NumerosEstaticos:
            Sena.setCategoria("NumerosEstaticos")
        Sena.setup(self.IIG5)
        self.IIG5.show()
    def retranslateUi(self, IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_1.setText(_translate("IG4_Aprendizaje", "1"))
        self.boton_2.setText(_translate("IG4_Aprendizaje", "2"))
        self.boton_3.setText(_translate("IG4_Aprendizaje", "3"))
        self.boton_4.setText(_translate("IG4_Aprendizaje", "4"))
        self.boton_5.setText(_translate("IG4_Aprendizaje", "5"))
        self.boton_6.setText(_translate("IG4_Aprendizaje", "6"))
        self.boton_7.setText(_translate("IG4_Aprendizaje", "7"))
        self.boton_8.setText(_translate("IG4_Aprendizaje", "8"))
        self.boton_9.setText(_translate("IG4_Aprendizaje", "9"))
        self.boton_10.setText(_translate("IG4_Aprendizaje", "10"))
        self.boton_20.setText(_translate("IG4_Aprendizaje", "20"))
        self.boton_30.setText(_translate("IG4_Aprendizaje", "30"))
        self.boton_40.setText(_translate("IG4_Aprendizaje", "40"))
        self.boton_50.setText(_translate("IG4_Aprendizaje", "50"))
        self.boton_60.setText(_translate("IG4_Aprendizaje", "60"))
        self.boton_70.setText(_translate("IG4_Aprendizaje", "70"))
        self.boton_80.setText(_translate("IG4_Aprendizaje", "80"))
        self.boton_90.setText(_translate("IG4_Aprendizaje", "90"))
        self.boton_100.setText(_translate("IG4_Aprendizaje", "100"))
        

        # Las comentadas son señas dinámicas