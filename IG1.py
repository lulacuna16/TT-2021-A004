# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG1.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import IG2 as G2
from Clases.Usuario import Usuario
import os

class Ui_IG1_Bienvenida(object):
    def setupUi(self, IG1_Bienvenida):
        IG1_Bienvenida.setObjectName("IG1_Bienvenida")
        IG1_Bienvenida.resize(499, 284)
        IG1_Bienvenida.setLayoutDirection(QtCore.Qt.LeftToRight)
        IG1_Bienvenida.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 175, 247);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(IG1_Bienvenida)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(IG1_Bienvenida)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LabelBienvenida = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LabelBienvenida.setFont(font)
        self.LabelBienvenida.setStyleSheet("font: 28pt \"Segoe Print\";\n"
"background-color: rgb(255, 175, 247);\n"
"color: rgb(0, 0, 0);")
        self.LabelBienvenida.setTextFormat(QtCore.Qt.RichText)
        self.LabelBienvenida.setScaledContents(True)
        self.LabelBienvenida.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelBienvenida.setObjectName("LabelBienvenida")
        self.gridLayout.addWidget(self.LabelBienvenida, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(IG1_Bienvenida)
        self.frame_2.setEnabled(True)
        self.frame_2.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("Croissant One")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(255, 175, 247);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(125, -1, 125, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)
        self.botonUsuario1 = QtWidgets.QPushButton(self.frame_2)
        self.botonUsuario1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botonUsuario1.setFont(font)
        self.botonUsuario1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botonUsuario1.setStyleSheet("QPushButton{\n"
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
        self.botonUsuario1.setObjectName("botonUsuario1")
        self.IUsuario1(IG1_Bienvenida)
        self.gridLayout_3.addWidget(self.botonUsuario1, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(IG1_Bienvenida)
        QtCore.QMetaObject.connectSlotsByName(IG1_Bienvenida)

    def IUsuario1(self,IG1_Bienvenida):
        self.botonUsuario1.clicked.connect(lambda:self.abrirIG2(IG1_Bienvenida))
    def abrirIG2(self,IG1_Bienvenida):
        IG1_Bienvenida.hide()
        self.IIG2=QtWidgets.QWidget()
        ui = G2.Ui_IG2_MenuUsuario()
        ui.setupUi(self.IIG2)
        self.IIG2.show()

    def nombreUsuario(self,id):
        usuario = Usuario()
        path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        # print(path)
        # print(os.path.exists(path))
        usuario.setBD(path)
        usuario.obtenerUsuarioBDId(id)
        # print(usuario)
        return usuario.nombre
    def retranslateUi(self, IG1_Bienvenida):
        _translate = QtCore.QCoreApplication.translate
        IG1_Bienvenida.setWindowTitle(_translate("IG1_Bienvenida", "Bienvenido"))
        self.LabelBienvenida.setText(_translate("IG1_Bienvenida", "Selecciona un usuario"))
        self.botonUsuario1.setText(_translate("IG1_Bienvenida",self.nombreUsuario(1)))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IG1_Bienvenida = QtWidgets.QWidget()
    ui = Ui_IG1_Bienvenida()
    ui.setupUi(IG1_Bienvenida)
    IG1_Bienvenida.show()
    app.exec_()
