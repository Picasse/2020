# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mincuadrados.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 299)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(200, 0, 211, 291))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 40, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 200, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 140, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QtCore.QRect(430, 250, 261, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setGeometry(QtCore.QRect(429, 9, 261, 211))
        self.MplWidget.setObjectName("MplWidget")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Lineal"))
        self.comboBox.setItemText(1, _translate("Form", "Parabolica"))
        self.comboBox.setItemText(2, _translate("Form", "Polinomica"))
        self.comboBox.setItemText(3, _translate("Form", "Exponencial"))
        self.comboBox.setItemText(4, _translate("Form", "Logaritmica"))
        self.label.setText(_translate("Form", "Numero de datos:"))
        self.pushButton.setText(_translate("Form", "Leer"))
        self.label_2.setText(_translate("Form", "grado de polinomio:"))
        self.label_3.setText(_translate("Form", "curva de ajuste:"))
        self.label_4.setText(_translate("Form", "R="))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

