from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
import os


class IG_Abecedario(object):
    def iniciar_Abecedario(self,widgetAbecedario):
        self.imagen_A = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_A.setGeometry(QtCore.QRect(30, 20, 51, 41))
        self.imagen_A.setObjectName("imagen_A")
        self.boton_A = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_A.setGeometry(QtCore.QRect(20, 70, 75, 31))
        self.boton_A.setStyleSheet("QPushButton{\n"
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
        self.boton_A.setObjectName("boton_A")
        self.imagen_B = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_B.setGeometry(QtCore.QRect(130, 20, 51, 41))
        self.imagen_B.setObjectName("imagen_B")
        self.boton_B = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_B.setGeometry(QtCore.QRect(110, 70, 75, 31))
        self.boton_B.setStyleSheet("QPushButton{\n"
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
        self.boton_B.setObjectName("boton_B")
        self.imagen_C = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_C.setGeometry(QtCore.QRect(210, 20, 51, 41))
        self.imagen_C.setObjectName("imagen_C")
        self.boton_C = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_C.setGeometry(QtCore.QRect(200, 70, 75, 31))
        self.boton_C.setStyleSheet("QPushButton{\n"
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
        self.boton_C.setObjectName("boton_C")
        self.imagen_D = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_D.setGeometry(QtCore.QRect(310, 20, 51, 41))
        self.imagen_D.setObjectName("imagen_D")
        self.boton_D = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_D.setGeometry(QtCore.QRect(290, 70, 75, 31))
        self.boton_D.setStyleSheet("QPushButton{\n"
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
        self.boton_D.setObjectName("boton_D")
        self.imagen_E = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_E.setGeometry(QtCore.QRect(400, 20, 51, 41))
        self.imagen_E.setObjectName("imagen_E")
        self.boton_E = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_E.setGeometry(QtCore.QRect(380, 70, 75, 31))
        self.boton_E.setStyleSheet("QPushButton{\n"
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
        self.boton_E.setObjectName("boton_E")
        self.imagen_F = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_F.setGeometry(QtCore.QRect(490, 20, 51, 41))
        self.imagen_F.setObjectName("imagen_F")
        self.boton_F = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_F.setGeometry(QtCore.QRect(470, 70, 75, 31))
        self.boton_F.setStyleSheet("QPushButton{\n"
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
        self.boton_F.setObjectName("boton_F")
        self.imagen_G = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_G.setGeometry(QtCore.QRect(580, 20, 51, 41))
        self.imagen_G.setObjectName("imagen_G")
        self.boton_G = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_G.setGeometry(QtCore.QRect(560, 70, 75, 31))
        self.boton_G.setStyleSheet("QPushButton{\n"
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
        self.boton_G.setObjectName("boton_G")
        self.imagen_H = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_H.setGeometry(QtCore.QRect(660, 20, 51, 41))
        self.imagen_H.setObjectName("imagen_H")
        self.boton_H = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_H.setGeometry(QtCore.QRect(650, 70, 75, 31))
        self.boton_H.setStyleSheet("QPushButton{\n"
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
                                   "}\n"
                                   "")
        self.boton_H.setObjectName("boton_H")
        self.imagen_I = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_I.setGeometry(QtCore.QRect(750, 20, 51, 41))
        self.imagen_I.setObjectName("imagen_I")
        self.boton_I = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_I.setGeometry(QtCore.QRect(740, 70, 75, 31))
        self.boton_I.setStyleSheet("QPushButton{\n"
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
        self.boton_I.setObjectName("boton_I")
        self.imagen_J = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_J.setGeometry(QtCore.QRect(30, 120, 51, 41))
        self.imagen_J.setObjectName("imagen_J")
        self.boton_J = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_J.setGeometry(QtCore.QRect(20, 170, 75, 31))
        self.boton_J.setStyleSheet("QPushButton{\n"
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
        self.boton_J.setObjectName("boton_J")
        self.imagen_K = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_K.setGeometry(QtCore.QRect(130, 120, 51, 41))
        self.imagen_K.setObjectName("imagen_K")
        self.boton_K = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_K.setGeometry(QtCore.QRect(110, 170, 75, 31))
        self.boton_K.setStyleSheet("QPushButton{\n"
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
        self.boton_K.setObjectName("boton_K")
        self.imagen_L = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_L.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_L.setObjectName("imagen_L")
        self.boton_L = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_L.setGeometry(QtCore.QRect(200, 170, 75, 31))
        self.boton_L.setStyleSheet("QPushButton{\n"
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
        self.boton_L.setObjectName("boton_L")
        self.imagen_M = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_M.setGeometry(QtCore.QRect(310, 120, 51, 41))
        self.imagen_M.setObjectName("imagen_M")
        self.boton_M = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_M.setGeometry(QtCore.QRect(290, 170, 75, 31))
        self.boton_M.setStyleSheet("QPushButton{\n"
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
        self.boton_M.setObjectName("boton_M")
        self.imagen_N = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_N.setGeometry(QtCore.QRect(400, 120, 51, 41))
        self.imagen_N.setObjectName("imagen_N")
        self.boton_N = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_N.setGeometry(QtCore.QRect(380, 170, 75, 31))
        self.boton_N.setStyleSheet("QPushButton{\n"
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
        self.boton_N.setObjectName("boton_N")
        self.imagen_NQ = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_NQ.setGeometry(QtCore.QRect(480, 120, 51, 41))
        self.imagen_NQ.setObjectName("imagen_NQ")
        self.boton_NQ = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_NQ.setGeometry(QtCore.QRect(470, 170, 75, 31))
        self.boton_NQ.setStyleSheet("QPushButton{\n"
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
        self.boton_NQ.setObjectName("boton_NQ")
        self.imagen_O = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_O.setGeometry(QtCore.QRect(580, 120, 51, 41))
        self.imagen_O.setObjectName("imagen_O")
        self.boton_O = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_O.setGeometry(QtCore.QRect(560, 170, 75, 31))
        self.boton_O.setStyleSheet("QPushButton{\n"
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
        self.boton_O.setObjectName("boton_O")
        self.imagen_P = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_P.setGeometry(QtCore.QRect(660, 120, 51, 41))
        self.imagen_P.setObjectName("imagen_P")
        self.boton_P = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_P.setGeometry(QtCore.QRect(650, 170, 75, 31))
        self.boton_P.setStyleSheet("QPushButton{\n"
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
        self.boton_P.setObjectName("boton_P")
        self.imagen_Q = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_Q.setGeometry(QtCore.QRect(750, 120, 51, 41))
        self.imagen_Q.setObjectName("imagen_Q")
        self.boton_Q = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_Q.setGeometry(QtCore.QRect(740, 170, 75, 31))
        self.boton_Q.setStyleSheet("QPushButton{\n"
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
        self.boton_Q.setObjectName("boton_Q")
        self.imagen_R = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_R.setGeometry(QtCore.QRect(30, 220, 51, 41))
        self.imagen_R.setObjectName("imagen_R")
        self.boton_R = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_R.setGeometry(QtCore.QRect(20, 270, 75, 31))
        self.boton_R.setStyleSheet("QPushButton{\n"
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
        self.boton_R.setObjectName("boton_R")
        self.imagen_S = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_S.setGeometry(QtCore.QRect(130, 220, 51, 41))
        self.imagen_S.setObjectName("imagen_S")
        self.boton_S = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_S.setGeometry(QtCore.QRect(110, 270, 75, 31))
        self.boton_S.setStyleSheet("QPushButton{\n"
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
        self.boton_S.setObjectName("boton_S")
        self.imagen_T = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_T.setGeometry(QtCore.QRect(220, 220, 51, 41))
        self.imagen_T.setObjectName("imagen_T")
        self.boton_T = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_T.setGeometry(QtCore.QRect(200, 270, 75, 31))
        self.boton_T.setStyleSheet("QPushButton{\n"
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
        self.boton_T.setObjectName("boton_T")
        self.imagen_U = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_U.setGeometry(QtCore.QRect(310, 220, 51, 41))
        self.imagen_U.setObjectName("imagen_U")
        self.boton_U = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_U.setGeometry(QtCore.QRect(290, 270, 75, 31))
        self.boton_U.setStyleSheet("QPushButton{\n"
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
        self.boton_U.setObjectName("boton_U")
        self.imagen_V = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_V.setGeometry(QtCore.QRect(400, 220, 51, 41))
        self.imagen_V.setObjectName("imagen_V")
        self.boton_V = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_V.setGeometry(QtCore.QRect(380, 270, 75, 31))
        self.boton_V.setStyleSheet("QPushButton{\n"
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
        self.boton_V.setObjectName("boton_V")
        self.imagen_W = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_W.setGeometry(QtCore.QRect(490, 220, 51, 41))
        self.imagen_W.setObjectName("imagen_W")
        self.boton_W = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_W.setGeometry(QtCore.QRect(470, 270, 75, 31))
        self.boton_W.setStyleSheet("QPushButton{\n"
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
        self.boton_W.setObjectName("boton_W")
        self.imagen_X = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_X.setGeometry(QtCore.QRect(570, 220, 51, 41))
        self.imagen_X.setObjectName("imagen_X")
        self.boton_X = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_X.setGeometry(QtCore.QRect(560, 270, 75, 31))
        self.boton_X.setStyleSheet("QPushButton{\n"
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
        self.boton_X.setObjectName("boton_X")
        self.imagen_Y = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_Y.setGeometry(QtCore.QRect(660, 220, 51, 41))
        self.imagen_Y.setObjectName("imagen_Y")
        self.boton_Y = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_Y.setGeometry(QtCore.QRect(650, 270, 75, 31))
        self.boton_Y.setStyleSheet("QPushButton{\n"
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
        self.boton_Y.setObjectName("boton_Y")
        self.imagen_Z = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_Z.setGeometry(QtCore.QRect(750, 220, 51, 41))
        self.imagen_Z.setObjectName("imagen_Z")
        self.boton_Z = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_Z.setGeometry(QtCore.QRect(740, 270, 75, 31))
        self.boton_Z.setStyleSheet("QPushButton{\n"
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
        self.boton_Z.setObjectName("boton_Z")
        self.label = QtWidgets.QLabel(widgetAbecedario)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Iconos/a.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widgetAbecedario)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 71, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Iconos/b.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(widgetAbecedario)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 71, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Iconos/c.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(widgetAbecedario)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 71, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Iconos/d.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(widgetAbecedario)
        self.label_5.setGeometry(QtCore.QRect(380, 10, 71, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Iconos/e.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(widgetAbecedario)
        self.label_6.setGeometry(QtCore.QRect(470, 10, 71, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Iconos/f.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(widgetAbecedario)
        self.label_7.setGeometry(QtCore.QRect(560, 10, 71, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Iconos/g.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(widgetAbecedario)
        self.label_8.setGeometry(QtCore.QRect(650, 10, 71, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Iconos/h.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(widgetAbecedario)
        self.label_9.setGeometry(QtCore.QRect(20, 110, 71, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Iconos/j.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(widgetAbecedario)
        self.label_10.setGeometry(QtCore.QRect(110, 110, 71, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Iconos/k.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(widgetAbecedario)
        self.label_11.setGeometry(QtCore.QRect(200, 110, 71, 51))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Iconos/l.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(widgetAbecedario)
        self.label_12.setGeometry(QtCore.QRect(280, 110, 91, 51))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Iconos/m.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(widgetAbecedario)
        self.label_13.setGeometry(QtCore.QRect(380, 110, 71, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Iconos/n.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(widgetAbecedario)
        self.label_14.setGeometry(QtCore.QRect(470, 110, 71, 51))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Iconos/ñ.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(widgetAbecedario)
        self.label_15.setGeometry(QtCore.QRect(560, 110, 71, 51))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Iconos/o.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(widgetAbecedario)
        self.label_16.setGeometry(QtCore.QRect(650, 110, 71, 51))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("Iconos/p.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(widgetAbecedario)
        self.label_17.setGeometry(QtCore.QRect(20, 210, 71, 51))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("Iconos/r.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(widgetAbecedario)
        self.label_18.setGeometry(QtCore.QRect(110, 210, 71, 51))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("Iconos/s.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(widgetAbecedario)
        self.label_19.setGeometry(QtCore.QRect(200, 210, 71, 51))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("Iconos/t.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(widgetAbecedario)
        self.label_20.setGeometry(QtCore.QRect(290, 210, 71, 51))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("Iconos/u.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(widgetAbecedario)
        self.label_21.setGeometry(QtCore.QRect(380, 210, 71, 51))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("Iconos/v.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(widgetAbecedario)
        self.label_22.setGeometry(QtCore.QRect(460, 210, 91, 51))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("Iconos/w.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(widgetAbecedario)
        self.label_23.setGeometry(QtCore.QRect(560, 210, 71, 51))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("Iconos/x.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(widgetAbecedario)
        self.label_24.setGeometry(QtCore.QRect(650, 210, 71, 51))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Iconos/y.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(widgetAbecedario)
        self.label_25.setGeometry(QtCore.QRect(740, 10, 71, 51))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Iconos/i.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(widgetAbecedario)
        self.label_26.setGeometry(QtCore.QRect(740, 110, 71, 51))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("Iconos/q.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(widgetAbecedario)
        self.label_27.setGeometry(QtCore.QRect(740, 210, 71, 51))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("Iconos/z.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.boton_A.clicked.connect(lambda: self.buttonClicked(self.boton_A))
        self.boton_B.clicked.connect(lambda: self.buttonClicked(self.boton_B))
        self.boton_C.clicked.connect(lambda: self.buttonClicked(self.boton_C))
        self.boton_D.clicked.connect(lambda: self.buttonClicked(self.boton_D))
        self.boton_E.clicked.connect(lambda: self.buttonClicked(self.boton_E))
        self.boton_F.clicked.connect(lambda: self.buttonClicked(self.boton_F))
        self.boton_G.clicked.connect(lambda: self.buttonClicked(self.boton_G))
        self.boton_H.clicked.connect(lambda: self.buttonClicked(self.boton_H))
        self.boton_I.clicked.connect(lambda: self.buttonClicked(self.boton_I))
        #self.boton_J.clicked.connect(lambda: self.buttonClicked(self.boton_J))
        #self.boton_K.clicked.connect(lambda: self.buttonClicked(self.boton_K))
        self.boton_L.clicked.connect(lambda: self.buttonClicked(self.boton_L))
        self.boton_M.clicked.connect(lambda: self.buttonClicked(self.boton_M))
        self.boton_N.clicked.connect(lambda: self.buttonClicked(self.boton_N))
        #self.boton_NQ.clicked.connect(lambda: self.buttonClicked(self.boton_NQ)) #Ñ
        self.boton_O.clicked.connect(lambda: self.buttonClicked(self.boton_O))
        self.boton_P.clicked.connect(lambda: self.buttonClicked(self.boton_P))
        #self.boton_Q.clicked.connect(lambda: self.buttonClicked(self.boton_Q))
        self.boton_R.clicked.connect(lambda: self.buttonClicked(self.boton_R))
        self.boton_S.clicked.connect(lambda: self.buttonClicked(self.boton_S))
        self.boton_T.clicked.connect(lambda: self.buttonClicked(self.boton_T))
        self.boton_U.clicked.connect(lambda: self.buttonClicked(self.boton_U))
        self.boton_V.clicked.connect(lambda: self.buttonClicked(self.boton_V))
        self.boton_W.clicked.connect(lambda: self.buttonClicked(self.boton_W))
        #self.boton_X.clicked.connect(lambda: self.buttonClicked(self.boton_X))
        self.boton_Y.clicked.connect(lambda: self.buttonClicked(self.boton_Y))
        #self.boton_Z.clicked.connect(lambda: self.buttonClicked(self.boton_Z))

    def buttonClicked(self, boton):
        self.IIG5=QtWidgets.QWidget()
        Sena = IGSena.Ui_IG5_Sena()
        Sena.setupUi(self.IIG5)
        Sena.setNombre(boton.text())
        ruta = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/") + "/videos/abecedario/")
        print(ruta)
        print(os.path.exists(ruta))
        ruta += boton.text() + ".wmv"
        print(os.path.exists(ruta))
        Sena.setPath(ruta)
        Sena.setup(self.IIG5)
        self.IIG5.show()
        #print(boton.text())
    def retranslateUiAbecedario(self,IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_A.setText(_translate("IG4_Aprendizaje", "A"))
        self.boton_B.setText(_translate("IG4_Aprendizaje", "B"))
        self.boton_C.setText(_translate("IG4_Aprendizaje", "C"))
        self.boton_D.setText(_translate("IG4_Aprendizaje", "D"))
        self.boton_E.setText(_translate("IG4_Aprendizaje", "E"))
        self.boton_F.setText(_translate("IG4_Aprendizaje", "F"))
        self.boton_G.setText(_translate("IG4_Aprendizaje", "G"))
        self.boton_H.setText(_translate("IG4_Aprendizaje", "H"))
        self.boton_I.setText(_translate("IG4_Aprendizaje", "I"))
        #self.boton_J.setText(_translate("IG4_Aprendizaje", "J"))
        #self.boton_K.setText(_translate("IG4_Aprendizaje", "K"))
        self.boton_L.setText(_translate("IG4_Aprendizaje", "L"))
        self.boton_M.setText(_translate("IG4_Aprendizaje", "M"))
        self.boton_N.setText(_translate("IG4_Aprendizaje", "N"))
        #self.boton_NQ.setText(_translate("IG4_Aprendizaje", "Ñ"))
        self.boton_O.setText(_translate("IG4_Aprendizaje", "O"))
        self.boton_P.setText(_translate("IG4_Aprendizaje", "P"))
        #self.boton_Q.setText(_translate("IG4_Aprendizaje", "Q"))
        self.boton_R.setText(_translate("IG4_Aprendizaje", "R"))
        self.boton_S.setText(_translate("IG4_Aprendizaje", "S"))
        self.boton_T.setText(_translate("IG4_Aprendizaje", "T"))
        self.boton_U.setText(_translate("IG4_Aprendizaje", "U"))
        self.boton_V.setText(_translate("IG4_Aprendizaje", "V"))
        self.boton_W.setText(_translate("IG4_Aprendizaje", "W"))
        #self.boton_X.setText(_translate("IG4_Aprendizaje", "X"))
        self.boton_Y.setText(_translate("IG4_Aprendizaje", "Y"))
        #self.boton_Z.setText(_translate("IG4_Aprendizaje", "Z"))

        #Las comentadas son señas dinámicas