# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 450)
        Form.setStyleSheet("background-color:rgb(235, 238, 255)")
        self.btn_auto_set = QtWidgets.QPushButton(Form)
        self.btn_auto_set.setGeometry(QtCore.QRect(380, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auto_set.setFont(font)
        self.btn_auto_set.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auto_set.setObjectName("btn_auto_set")
        self.lbl_auto_02 = QtWidgets.QLabel(Form)
        self.lbl_auto_02.setGeometry(QtCore.QRect(50, 100, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auto_02.setFont(font)
        self.lbl_auto_02.setStyleSheet("background-color:#fff;")
        self.lbl_auto_02.setObjectName("lbl_auto_02")
        self.cb_auto_speed = QtWidgets.QComboBox(Form)
        self.cb_auto_speed.setGeometry(QtCore.QRect(210, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_auto_speed.setFont(font)
        self.cb_auto_speed.setStyleSheet("background-color:#fff;")
        self.cb_auto_speed.setObjectName("cb_auto_speed")
        self.cb_auto_speed.addItem("")
        self.cb_auto_speed.addItem("")
        self.cb_auto_speed.addItem("")
        self.btn_auto_back = QtWidgets.QPushButton(Form)
        self.btn_auto_back.setGeometry(QtCore.QRect(210, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auto_back.setFont(font)
        self.btn_auto_back.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auto_back.setObjectName("btn_auto_back")
        self.btn_auto_start = QtWidgets.QPushButton(Form)
        self.btn_auto_start.setGeometry(QtCore.QRect(360, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auto_start.setFont(font)
        self.btn_auto_start.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auto_start.setObjectName("btn_auto_start")
        self.lbl_auto_01 = QtWidgets.QLabel(Form)
        self.lbl_auto_01.setGeometry(QtCore.QRect(30, 20, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_auto_01.setFont(font)
        self.lbl_auto_01.setStyleSheet("background-color:rgb(200, 255, 176);")
        self.lbl_auto_01.setObjectName("lbl_auto_01")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_auto_set.setText(_translate("Form", "Đặt"))
        self.lbl_auto_02.setText(_translate("Form", "Tốc độ phân loại"))
        self.cb_auto_speed.setItemText(0, _translate("Form", "Nhanh"))
        self.cb_auto_speed.setItemText(1, _translate("Form", "Thường"))
        self.cb_auto_speed.setItemText(2, _translate("Form", "Chậm"))
        self.btn_auto_back.setText(_translate("Form", "Quay lại"))
        self.btn_auto_start.setText(_translate("Form", "Bắt đầu"))
        self.lbl_auto_01.setText(_translate("Form", "Tự động"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
