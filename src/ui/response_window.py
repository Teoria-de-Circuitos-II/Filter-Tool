# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/response_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResponseDialog(object):
    def setupUi(self, ResponseDialog):
        ResponseDialog.setObjectName("ResponseDialog")
        ResponseDialog.resize(720, 260)
        self.buttonBox = QtWidgets.QDialogButtonBox(ResponseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 220, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(ResponseDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.error_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 5, 0, 1, 1)
        self.check_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.check_btn.setEnabled(True)
        self.check_btn.setObjectName("check_btn")
        self.gridLayout.addWidget(self.check_btn, 4, 0, 1, 1)
        self.resp_name_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.resp_name_txt.setEnabled(True)
        self.resp_name_txt.setObjectName("resp_name_txt")
        self.gridLayout.addWidget(self.resp_name_txt, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.minbox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.minbox.setDecimals(5)
        self.minbox.setMinimum(0.0)
        self.minbox.setMaximum(999999999.99999)
        self.minbox.setProperty("value", 0.0)
        self.minbox.setObjectName("minbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minbox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.maxbox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.maxbox.setDecimals(5)
        self.maxbox.setMaximum(999999999.99999)
        self.maxbox.setProperty("value", 1.0)
        self.maxbox.setObjectName("maxbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxbox)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.stepbox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.stepbox.setDecimals(5)
        self.stepbox.setProperty("value", 0.0001)
        self.stepbox.setObjectName("stepbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stepbox)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.input_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_txt.setEnabled(True)
        self.input_txt.setObjectName("input_txt")
        self.gridLayout.addWidget(self.input_txt, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(ResponseDialog)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(310, 10, 401, 241))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(ResponseDialog)
        self.buttonBox.accepted.connect(ResponseDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ResponseDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ResponseDialog)

    def retranslateUi(self, ResponseDialog):
        _translate = QtCore.QCoreApplication.translate
        ResponseDialog.setWindowTitle(_translate("ResponseDialog", "Dialog"))
        self.check_btn.setText(_translate("ResponseDialog", "Validar"))
        self.resp_name_txt.setPlaceholderText(_translate("ResponseDialog", "Function name"))
        self.label.setText(_translate("ResponseDialog", "Mínimo"))
        self.label_2.setText(_translate("ResponseDialog", "Máximo"))
        self.label_3.setText(_translate("ResponseDialog", "Intervalo"))
        self.input_txt.setPlaceholderText(_translate("ResponseDialog", "Function expression"))
        self.textBrowser.setHtml(_translate("ResponseDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AYUDA:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">delta # respuesta al impulso unitario</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">step # respuesta al escalón</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">np.heaviside(t0, a) # escalón unitario centrado en t=t0 y con valor 0&lt;a&lt;1 en t0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">np.sin(t) # seno</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">np.cos(t) # coseno</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">np.exp(t) # exponencial</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">signal.sawtooth(t, w) # diente de sierra con -1&lt;=w&lt;=1 (w=0.5 para triangular)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">signal.square(t, D) # señal cuadrada con ciclo de trabajo 0&lt;D&lt;1</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResponseDialog = QtWidgets.QDialog()
    ui = Ui_ResponseDialog()
    ui.setupUi(ResponseDialog)
    ResponseDialog.show()
    sys.exit(app.exec_())
