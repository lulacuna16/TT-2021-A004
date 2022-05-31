


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG_Instrucciones.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IG_Instrucciones(object):
    def setupUi(self, IG_Instrucciones):
        IG_Instrucciones.setObjectName("IG_Instrucciones")
        IG_Instrucciones.setMaximumSize(QtCore.QSize(823, 561))
        IG_Instrucciones.setMinimumSize(QtCore.QSize(823, 561))
        IG_Instrucciones.setStyleSheet("background-color: rgb(250, 215, 160);\n"
"")
        self.labelInicio = QtWidgets.QLabel(IG_Instrucciones)
        self.labelInicio.setGeometry(QtCore.QRect(250, 10, 291, 31))
        self.labelInicio.setStyleSheet("font: 16pt \"Segoe Print\";\n"
"color: rgb(156, 100, 12);")
        self.labelInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInicio.setObjectName("labelInicio")
        self.labelInstrucciones = QtWidgets.QLabel(IG_Instrucciones)
        self.labelInstrucciones.setGeometry(QtCore.QRect(30, 50, 761, 501))
        self.labelInstrucciones.setStyleSheet("font: 10pt \"Segoe Print\";\n"
"color: rgb(156, 100, 12);")
        self.labelInstrucciones.setTextFormat(QtCore.Qt.PlainText)
        self.labelInstrucciones.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelInstrucciones.setWordWrap(True)
        self.labelInstrucciones.setObjectName("labelInstrucciones")

        self.retranslateUi(IG_Instrucciones)
        QtCore.QMetaObject.connectSlotsByName(IG_Instrucciones)

    def retranslateUi(self, IG_Instrucciones):
        _translate = QtCore.QCoreApplication.translate
        IG_Instrucciones.setWindowTitle(_translate("IG_Instrucciones", "Instrucciones"))
        self.labelInicio.setText(_translate("IG_Instrucciones", "Para utilizar la aplicación:"))
        self.labelInstrucciones.setText(_translate("IG_Instrucciones", "1. Adopte una posición cómoda frente a su computadora.\n"
"\n"
"2. Asegúrese de que la distancia entre la cámara y usted sea la adecuada, de tal modo que se pueda captar sus manos o su cuerpo. Utilice la vista previa de la cámara como apoyo.\n"
"\n"
"3.Antes de validar la seña seleccionada, puede visualizar el videotutorial a la izquierda de la pantalla de la aplicación (puede utilizar los botones de Reproducir o Pausar las veces que desee).\n"
"\n"
"4.Para comenzar a validar la seña, presione el botón Verificar y espere a que termine el conteo que se muestra en la vista previa de la cámara.\n"
"*Mientras la aplicación está verificando su movimiento, el botón Verificar se deshabilita y aparece la leyenda \"Verificando...\".\n"
"\n"
"5.Si se trata de una seña dinámica, haga el movimiento de manera gradual y lenta, para que el sistema pueda leerlo de manera correcta.\n"
"**Si la seña no se ha podido verificar en 20 segundos (señas estáticas) o 30 segundos (señas dinámicas) en la vista previa aparecerá un texto notificándole.\n"
"\n"
"6. Cuando se haya validado la seña, la vista previa de la cámara se detendrá y arriba de ella aparecerá una mensaje que indique que la seña fue correcta.\n"
"\n"
"7.Para regresar a la Sección de Aprendizaje presione el botón Salir. "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IG_Instrucciones = QtWidgets.QWidget()
    ui = Ui_IG_Instrucciones()
    ui.setupUi(IG_Instrucciones)
    IG_Instrucciones.show()
    sys.exit(app.exec_())
