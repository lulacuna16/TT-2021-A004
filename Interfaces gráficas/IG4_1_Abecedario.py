
from PyQt5 import QtCore, QtGui, QtWidgets
import IG5 as IGSena
import os

class IG_Abecedario(object):
    def iniciar_Abecedario(self,widgetAbecedario):
        self.imagen_A = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_A.setGeometry(QtCore.QRect(30, 20, 51, 41))
        self.imagen_A.setObjectName("imagen_A")
        self.boton_A = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_A.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.boton_A.setObjectName("boton_A")
        self.imagen_B = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_B.setGeometry(QtCore.QRect(130, 20, 51, 41))
        self.imagen_B.setObjectName("imagen_B")
        self.boton_B = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_B.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.boton_B.setObjectName("boton_B")
        self.imagen_C = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_C.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.imagen_C.setObjectName("imagen_C")
        self.boton_C = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_C.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.boton_C.setObjectName("boton_C")
        self.imagen_D = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_D.setGeometry(QtCore.QRect(310, 20, 51, 41))
        self.imagen_D.setObjectName("imagen_D")
        self.boton_D = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_D.setGeometry(QtCore.QRect(300, 70, 75, 23))
        self.boton_D.setObjectName("boton_D")
        self.imagen_E = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_E.setGeometry(QtCore.QRect(410, 20, 51, 41))
        self.imagen_E.setObjectName("imagen_E")
        self.boton_E = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_E.setGeometry(QtCore.QRect(400, 70, 75, 23))
        self.boton_E.setObjectName("boton_E")
        self.imagen_F = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_F.setGeometry(QtCore.QRect(510, 20, 51, 41))
        self.imagen_F.setObjectName("imagen_F")
        self.boton_F = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_F.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.boton_F.setObjectName("boton_F")
        self.imagen_G = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_G.setGeometry(QtCore.QRect(610, 20, 51, 41))
        self.imagen_G.setObjectName("imagen_G")
        self.boton_G = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_G.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.boton_G.setObjectName("boton_G")
        self.imagen_H = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_H.setGeometry(QtCore.QRect(710, 20, 51, 41))
        self.imagen_H.setObjectName("imagen_H")
        self.boton_H = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_H.setGeometry(QtCore.QRect(700, 70, 75, 23))
        self.boton_H.setObjectName("boton_H")
        self.imagen_I = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_I.setGeometry(QtCore.QRect(810, 20, 51, 41))
        self.imagen_I.setObjectName("imagen_I")
        self.boton_I = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_I.setGeometry(QtCore.QRect(800, 70, 75, 23))
        self.boton_I.setObjectName("boton_I")
        #self.imagen_J = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_J.setGeometry(QtCore.QRect(30, 120, 51, 41))
        #self.imagen_J.setObjectName("imagen_J")
        #self.boton_J = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_J.setGeometry(QtCore.QRect(20, 170, 75, 23))
        #self.boton_J.setObjectName("boton_J")
        #self.imagen_K = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_K.setGeometry(QtCore.QRect(130, 120, 51, 41))
        #self.imagen_K.setObjectName("imagen_K")
        #self.boton_K = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_K.setGeometry(QtCore.QRect(120, 170, 75, 23))
        #self.boton_K.setObjectName("boton_K")
        self.imagen_L = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_L.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.imagen_L.setObjectName("imagen_L")
        self.boton_L = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_L.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.boton_L.setObjectName("boton_L")
        self.imagen_M = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_M.setGeometry(QtCore.QRect(310, 120, 51, 41))
        self.imagen_M.setObjectName("imagen_M")
        self.boton_M = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_M.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.boton_M.setObjectName("boton_M")
        self.imagen_N = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_N.setGeometry(QtCore.QRect(410, 120, 51, 41))
        self.imagen_N.setObjectName("imagen_N")
        self.boton_N = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_N.setGeometry(QtCore.QRect(400, 170, 75, 23))
        self.boton_N.setObjectName("boton_N")
        #self.imagen_NQ = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_NQ.setGeometry(QtCore.QRect(510, 120, 51, 41))
        #self.imagen_NQ.setObjectName("imagen_NQ")
        #self.boton_NQ = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_NQ.setGeometry(QtCore.QRect(500, 170, 75, 23))
        #self.boton_NQ.setObjectName("boton_NQ")
        self.imagen_O = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_O.setGeometry(QtCore.QRect(610, 120, 51, 41))
        self.imagen_O.setObjectName("imagen_O")
        self.boton_O = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_O.setGeometry(QtCore.QRect(600, 170, 75, 23))
        self.boton_O.setObjectName("boton_O")
        self.imagen_P = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_P.setGeometry(QtCore.QRect(710, 120, 51, 41))
        self.imagen_P.setObjectName("imagen_P")
        self.boton_P = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_P.setGeometry(QtCore.QRect(700, 170, 75, 23))
        self.boton_P.setObjectName("boton_P")
        #self.imagen_Q = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_Q.setGeometry(QtCore.QRect(810, 120, 51, 41))
        #self.imagen_Q.setObjectName("imagen_Q")
        #self.boton_Q = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_Q.setGeometry(QtCore.QRect(800, 170, 75, 23))
        #self.boton_Q.setObjectName("boton_Q")
        self.imagen_R = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_R.setGeometry(QtCore.QRect(30, 220, 51, 41))
        self.imagen_R.setObjectName("imagen_R")
        self.boton_R = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_R.setGeometry(QtCore.QRect(20, 270, 75, 23))
        self.boton_R.setObjectName("boton_R")
        self.imagen_S = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_S.setGeometry(QtCore.QRect(130, 220, 51, 41))
        self.imagen_S.setObjectName("imagen_S")
        self.boton_S = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_S.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.boton_S.setObjectName("boton_S")
        self.imagen_T = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_T.setGeometry(QtCore.QRect(220, 220, 51, 41))
        self.imagen_T.setObjectName("imagen_T")
        self.boton_T = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_T.setGeometry(QtCore.QRect(210, 270, 75, 23))
        self.boton_T.setObjectName("boton_T")
        self.imagen_U = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_U.setGeometry(QtCore.QRect(310, 220, 51, 41))
        self.imagen_U.setObjectName("imagen_U")
        self.boton_U = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_U.setGeometry(QtCore.QRect(300, 270, 75, 23))
        self.boton_U.setObjectName("boton_U")
        self.imagen_V = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_V.setGeometry(QtCore.QRect(410, 220, 51, 41))
        self.imagen_V.setObjectName("imagen_V")
        self.boton_V = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_V.setGeometry(QtCore.QRect(400, 270, 75, 23))
        self.boton_V.setObjectName("boton_V")
        self.imagen_W = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_W.setGeometry(QtCore.QRect(510, 220, 51, 41))
        self.imagen_W.setObjectName("imagen_W")
        self.boton_W = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_W.setGeometry(QtCore.QRect(500, 270, 75, 23))
        self.boton_W.setObjectName("boton_W")
        #self.imagen_X = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_X.setGeometry(QtCore.QRect(610, 220, 51, 41))
        #self.imagen_X.setObjectName("imagen_X")
        #self.boton_X = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_X.setGeometry(QtCore.QRect(600, 270, 75, 23))
        #self.boton_X.setObjectName("boton_X")
        self.imagen_Y = QtWidgets.QGraphicsView(widgetAbecedario)
        self.imagen_Y.setGeometry(QtCore.QRect(710, 220, 51, 41))
        self.imagen_Y.setObjectName("imagen_Y")
        self.boton_Y = QtWidgets.QPushButton(widgetAbecedario)
        self.boton_Y.setGeometry(QtCore.QRect(700, 270, 75, 23))
        self.boton_Y.setObjectName("boton_Y")
        #self.imagen_Z = QtWidgets.QGraphicsView(widgetAbecedario)
        #self.imagen_Z.setGeometry(QtCore.QRect(810, 220, 51, 41))
        #self.imagen_Z.setObjectName("imagen_Z")
        #self.boton_Z = QtWidgets.QPushButton(widgetAbecedario)
        #self.boton_Z.setGeometry(QtCore.QRect(800, 270, 75, 23))
        #self.boton_Z.setObjectName("boton_Z")
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
        ruta = os.getcwd().replace("\\","/") + "/Interfaces gráficas/videos/abecedario/"
        ruta += boton.text() + ".wmv"
        Sena.setPath(ruta)
        Sena.setup(self.IIG5)
        self.IIG5.show()
        #print(boton.text())
    def retranslateUiAbecedario(self,IG4_Aprendizaje):
        _translate = QtCore.QCoreApplication.translate
        IG4_Aprendizaje.setWindowTitle(_translate("IG4_Aprendizaje", "Form"))
        self.boton_A.setText(_translate("IG4_Aprendizaje","A"))
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