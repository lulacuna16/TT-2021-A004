# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import IG1 as G1
import IG3 as G3
import IG4 as G4
from Clases.Usuario import Usuario
import os

class Ui_IG2_MenuUsuario(object):
    def setupUi(self, IG2_MenuUsuario):
        IG2_MenuUsuario.setObjectName("IG2_MenuUsuario")
        IG2_MenuUsuario.resize(515, 303)
        IG2_MenuUsuario.setStyleSheet("QWidget{\n"
                                      "background-color: rgb(255, 175, 247);\n"
                                      "}")
        self.labelBienvenida = QtWidgets.QLabel(IG2_MenuUsuario)
        self.labelBienvenida.setGeometry(QtCore.QRect(30, 50, 191, 41))
        self.labelBienvenida.setStyleSheet("font: 16pt \"Segoe Print\";")
        self.labelBienvenida.setObjectName("labelBienvenida")
        self.labelNombreUsuario = QtWidgets.QLabel(IG2_MenuUsuario)
        self.labelNombreUsuario.setGeometry(QtCore.QRect(70, 120, 111, 61))
        self.labelNombreUsuario.setStyleSheet("font: 16pt \"Segoe Print\";")
        self.labelNombreUsuario.setObjectName("labelNombreUsuario")
        self.botonPracticar = QtWidgets.QPushButton(IG2_MenuUsuario)
        self.botonPracticar.setGeometry(QtCore.QRect(290, 110, 151, 23))
        self.botonPracticar.setStyleSheet("QPushButton{\n"
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
        self.botonPracticar.setObjectName("botonPracticar")
        self.botonAprender = QtWidgets.QPushButton(IG2_MenuUsuario)
        self.botonAprender.setGeometry(QtCore.QRect(290, 50, 151, 23))
        self.botonAprender.setStyleSheet("QPushButton{\n"
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
        self.botonAprender.setObjectName("botonAprender")
        self.botonModificarPerfil = QtWidgets.QPushButton(IG2_MenuUsuario)
        self.botonModificarPerfil.setGeometry(QtCore.QRect(290, 170, 151, 23))
        self.botonModificarPerfil.setStyleSheet("QPushButton{\n"
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
        self.botonModificarPerfil.setObjectName("botonModificarPerfil")
        self.botonRegresarInicio = QtWidgets.QPushButton(IG2_MenuUsuario)
        self.botonRegresarInicio.setGeometry(QtCore.QRect(180, 240, 151, 23))
        self.botonRegresarInicio.setStyleSheet("QPushButton{\n"
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
        self.botonRegresarInicio.setObjectName("botonRegresarInicio")

        self.Eventos(IG2_MenuUsuario)
        self.retranslateUi(IG2_MenuUsuario)
        QtCore.QMetaObject.connectSlotsByName(IG2_MenuUsuario)

    def Eventos(self,IG2_MenuUsuario):
        self.botonModificarPerfil.clicked.connect(lambda:self.abrirIG3(IG2_MenuUsuario))
        self.botonRegresarInicio.clicked.connect(lambda:self.abrirIG1(IG2_MenuUsuario))
        self.botonAprender.clicked.connect(lambda: self.abrirIG4(IG2_MenuUsuario))

    def abrirIG3(self,IG2_MenuUsuario):
        IG2_MenuUsuario.hide()
        self.IIG3=QtWidgets.QWidget()
        ui = G3.Ui_IG3_ModificacionPerfil()
        ui.setIDUsuario(self.id_usuario)
        ui.setupUi(self.IIG3)
        self.IIG3.show()

    def abrirIG1(self,IG2_MenuUsuario):
        IG2_MenuUsuario.hide()
        self.IIG1=QtWidgets.QWidget()
        ui = G1.Ui_IG1_Bienvenida()
        ui.setupUi(self.IIG1)
        self.IIG1.show()

    def abrirIG4(self,IG2_MenuUsuario):
        IG2_MenuUsuario.hide()
        self.IIG4=QtWidgets.QWidget()
        ui = G4.Ui_IG4_Aprendizaje()
        ui.setIDUsuario(self.id_usuario)
        ui.setupUi(self.IIG4)
        self.IIG4.show()

    def retranslateUi(self, IG2_MenuUsuario):
        _translate = QtCore.QCoreApplication.translate
        IG2_MenuUsuario.setWindowTitle(_translate("IG2_MenuUsuario", "Menú de usuario"))
        self.labelNombreUsuario.setText(_translate("IG2_MenuUsuario", self.nombreUsuario(self.id_usuario)))
        self.botonModificarPerfil.setText(_translate("IG2_MenuUsuario", "Modificar Perfil"))
        self.botonAprender.setText(_translate("IG2_MenuUsuario", "Aprender"))
        self.botonPracticar.setText(_translate("IG2_MenuUsuario", "Practicar"))
        self.botonRegresarInicio.setText(_translate("IG2_MenuUsuario", "Regresar a Inicio"))
        self.labelBienvenida.setText(_translate("IG2_MenuUsuario", "¡Que gusto verte!"))

    def nombreUsuario(self,id):
        usuario = Usuario()
        path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        usuario.setBD(path)
        usuario.obtenerUsuarioBDId(id)
        return usuario.nombre

    def setIDUsuario(self,id_usuario):
        self.id_usuario = id_usuario

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IG2_MenuUsuario = QtWidgets.QWidget()
    ui = Ui_IG2_MenuUsuario()
    ui.setupUi(IG2_MenuUsuario)
    IG2_MenuUsuario.show()
    app.exec_()
