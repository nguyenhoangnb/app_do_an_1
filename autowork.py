# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autowork.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 700)
        Form.setStyleSheet("background-color:rgb(235, 238, 255)")
        self.lbl_auw_02 = QtWidgets.QLabel(Form)
        self.lbl_auw_02.setGeometry(QtCore.QRect(220, 60, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_02.setFont(font)
        self.lbl_auw_02.setStyleSheet("background-color:#fff;")
        self.lbl_auw_02.setObjectName("lbl_auw_02")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(330, 110, 281, 181))
        self.frame.setStyleSheet("background-color:#fff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_auw_03 = QtWidgets.QLabel(Form)
        self.lbl_auw_03.setGeometry(QtCore.QRect(340, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_03.setFont(font)
        self.lbl_auw_03.setStyleSheet("background-color:#fff;")
        self.lbl_auw_03.setText("")
        self.lbl_auw_03.setObjectName("lbl_auw_03")
        self.btn_auw_stop = QtWidgets.QPushButton(Form)
        self.btn_auw_stop.setGeometry(QtCore.QRect(30, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_stop.setFont(font)
        self.btn_auw_stop.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auw_stop.setObjectName("btn_auw_stop")
        self.btn_auw_back = QtWidgets.QPushButton(Form)
        self.btn_auw_back.setGeometry(QtCore.QRect(30, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_back.setFont(font)
        self.btn_auw_back.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auw_back.setObjectName("btn_auw_back")
        self.btn_auw_change = QtWidgets.QPushButton(Form)
        self.btn_auw_change.setGeometry(QtCore.QRect(30, 140, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_change.setFont(font)
        self.btn_auw_change.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auw_change.setObjectName("btn_auw_change")
        self.tbl_auw = QtWidgets.QTableView(Form)
        self.tbl_auw.setGeometry(QtCore.QRect(170, 310, 541, 321))
        self.tbl_auw.setStyleSheet("background-color:rgb(251, 255, 205)")
        self.tbl_auw.setObjectName("tbl_auw")
        self.lbl_auw_04 = QtWidgets.QLabel(Form)
        self.lbl_auw_04.setGeometry(QtCore.QRect(60, 310, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_04.setFont(font)
        self.lbl_auw_04.setStyleSheet("background-color:#fff;")
        self.lbl_auw_04.setObjectName("lbl_auw_04")
        self.lbl_auw_01 = QtWidgets.QLabel(Form)
        self.lbl_auw_01.setGeometry(QtCore.QRect(30, 20, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_auw_01.setFont(font)
        self.lbl_auw_01.setStyleSheet("background-color:rgb(200, 255, 176);")
        self.lbl_auw_01.setObjectName("lbl_auw_01")
        self.btn_auw_continue = QtWidgets.QPushButton(Form)
        self.btn_auw_continue.setGeometry(QtCore.QRect(30, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_continue.setFont(font)
        self.btn_auw_continue.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.btn_auw_continue.setObjectName("btn_auw_continue")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_auw_02.setText(_translate("Form", "Loại hàng"))
        self.btn_auw_stop.setText(_translate("Form", "Tạm dừng"))
        self.btn_auw_back.setText(_translate("Form", "Quay lại"))
        self.btn_auw_change.setText(_translate("Form", "Chuyển chế độ"))
        self.lbl_auw_04.setText(_translate("Form", "Số lượng"))
        self.lbl_auw_01.setText(_translate("Form", "Tự động"))
        self.btn_auw_continue.setText(_translate("Form", "Tiếp tục"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
