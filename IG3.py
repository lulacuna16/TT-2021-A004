# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import IG2 as G2
from Clases.Usuario import Usuario
import os

class Ui_IG3_ModificacionPerfil(object):
    def setupUi(self, IG3_ModificacionPerfil):
        IG3_ModificacionPerfil.setObjectName("IG3_ModificacionPerfil")
        IG3_ModificacionPerfil.resize(503, 300)
        IG3_ModificacionPerfil.setStyleSheet("background-color: rgb(255, 175, 247);\n"
                                             "")
        self.labelNombreUsuario = QtWidgets.QLabel(IG3_ModificacionPerfil)
        self.labelNombreUsuario.setGeometry(QtCore.QRect(150, 30, 201, 21))
        self.labelNombreUsuario.setStyleSheet("font: 14pt \"Segoe Print\";")
        self.labelNombreUsuario.setObjectName("labelNombreUsuario")
        self.textNombreUsuario = QtWidgets.QLineEdit(IG3_ModificacionPerfil)
        self.textNombreUsuario.setGeometry(QtCore.QRect(150, 60, 191, 20))
        self.textNombreUsuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(0, 0, 0);\n"
                                             "font: 11pt \"Segoe Print\";")
        self.textNombreUsuario.setInputMask("")
        self.textNombreUsuario.setObjectName("textNombreUsuario")
        self.botonGuardar = QtWidgets.QPushButton(IG3_ModificacionPerfil)
        self.botonGuardar.setGeometry(QtCore.QRect(130, 140, 231, 31))
        self.botonGuardar.setStyleSheet("QPushButton{\n"
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
        self.botonGuardar.setObjectName("botonGuardar")
        self.botonCancelar = QtWidgets.QPushButton(IG3_ModificacionPerfil)
        self.botonCancelar.setGeometry(QtCore.QRect(130, 200, 231, 31))
        self.botonCancelar.setStyleSheet("QPushButton{\n"
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
        self.botonCancelar.setObjectName("botonCancelar")
        self.Eventos(IG3_ModificacionPerfil)

        self.retranslateUi(IG3_ModificacionPerfil)
        QtCore.QMetaObject.connectSlotsByName(IG3_ModificacionPerfil)

    def Eventos(self,IG3_ModificacionPerfil):
        self.botonCancelar.clicked.connect(lambda:self.abrirIG2(IG3_ModificacionPerfil))
        self.botonGuardar.clicked.connect(lambda: self.actualizarNombre(1,IG3_ModificacionPerfil))


    def abrirIG2(self,IG3_ModificacionPerfil):
        IG3_ModificacionPerfil.hide()
        self.IIG2=QtWidgets.QWidget()
        ui=G2.Ui_IG2_MenuUsuario()
        ui.setupUi(self.IIG2)
        self.IIG2.show()

    def actualizarNombre(self,id,IG3_ModificacionPerfil):
        nombre = self.textNombreUsuario.text()
        usuario = Usuario()
        usuario.nombre = nombre
        path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        usuario.setBD(path)
        usuario.actualizarUsuarioBDId(id)
        self.abrirIG2(IG3_ModificacionPerfil)

    def retranslateUi(self, IG3_ModificacionPerfil):
        _translate = QtCore.QCoreApplication.translate
        IG3_ModificacionPerfil.setWindowTitle(_translate("IG3_ModificacionPerfil", "Modificación de perfil"))
        self.labelNombreUsuario.setText(_translate("IG3_ModificacionPerfil", "Nombre Usuario:"))
        self.textNombreUsuario.setText(_translate("IG3_ModificacionPerfil", self.nombreUsuario(1)))
        self.botonGuardar.setText(_translate("IG3_ModificacionPerfil", "Guardar"))
        self.botonCancelar.setText(_translate("IG3_ModificacionPerfil", "Cancelar"))

    def nombreUsuario(self,id):
        usuario = Usuario()
        path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/Clases/senas.db"
        usuario.setBD(path)
        usuario.obtenerUsuarioBDId(id)
        return usuario.nombre

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IG3_ModificacionPerfil = QtWidgets.QWidget()
    ui = Ui_IG3_ModificacionPerfil()
    ui.setupUi(IG3_ModificacionPerfil)
    IG3_ModificacionPerfil.show()
    sys.exit(app.exec_())
