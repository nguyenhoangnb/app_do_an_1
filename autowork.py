# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autowork.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1166, 783)
        Form.setStyleSheet("background-color:rgb(235, 238, 255)")
        self.lbl_auw_02 = QtWidgets.QLabel(Form)
        self.lbl_auw_02.setGeometry(QtCore.QRect(290, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_02.setFont(font)
        self.lbl_auw_02.setStyleSheet("background-color:rgb(200, 239, 196);\n"
"border-radius:12px;")
        self.lbl_auw_02.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_auw_02.setObjectName("lbl_auw_02")
        self.btn_auw_stop = QtWidgets.QPushButton(Form)
        self.btn_auw_stop.setGeometry(QtCore.QRect(60, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_stop.setFont(font)
        self.btn_auw_stop.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:12px;")
        self.btn_auw_stop.setObjectName("btn_auw_stop")
        self.btn_auw_back = QtWidgets.QPushButton(Form)
        self.btn_auw_back.setGeometry(QtCore.QRect(60, 150, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_back.setFont(font)
        self.btn_auw_back.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:12px;")
        self.btn_auw_back.setObjectName("btn_auw_back")
        self.btn_auw_change = QtWidgets.QPushButton(Form)
        self.btn_auw_change.setGeometry(QtCore.QRect(60, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_change.setFont(font)
        self.btn_auw_change.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_auw_change.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:12px;")
        self.btn_auw_change.setObjectName("btn_auw_change")
        self.lbl_auw3 = QtWidgets.QLabel(Form)
        self.lbl_auw3.setGeometry(QtCore.QRect(90, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw3.setFont(font)
        self.lbl_auw3.setStyleSheet("background-color:rgb(232, 131, 131);\n"
"border-radius:10px;")
        self.lbl_auw3.setWordWrap(True)
        self.lbl_auw3.setObjectName("lbl_auw3")
        self.lbl_auw_01 = QtWidgets.QLabel(Form)
        self.lbl_auw_01.setGeometry(QtCore.QRect(60, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_auw_01.setFont(font)
        self.lbl_auw_01.setStyleSheet("background-color:rgb(200, 255, 176);\n"
"border-radius:20px;\n"
"")
        self.lbl_auw_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_auw_01.setObjectName("lbl_auw_01")
        self.btn_auw_continue = QtWidgets.QPushButton(Form)
        self.btn_auw_continue.setGeometry(QtCore.QRect(60, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_auw_continue.setFont(font)
        self.btn_auw_continue.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:12px;")
        self.btn_auw_continue.setObjectName("btn_auw_continue")
        self.tbl_auto_quantity = QtWidgets.QTableWidget(Form)
        self.tbl_auto_quantity.setGeometry(QtCore.QRect(230, 370, 421, 281))
        self.tbl_auto_quantity.setStyleSheet("background-color:rgb(251, 255, 205)")
        self.tbl_auto_quantity.setRowCount(5)
        self.tbl_auto_quantity.setColumnCount(4)
        self.tbl_auto_quantity.setObjectName("tbl_auto_quantity")
        self.lbl_img = QtWidgets.QLabel(Form)
        self.lbl_img.setGeometry(QtCore.QRect(300, 100, 320, 240))
        self.lbl_img.setStyleSheet("background-color:#fff;")
        self.lbl_img.setText("")
        self.lbl_img.setObjectName("lbl_img")
        self.lbl_auw_3 = QtWidgets.QLabel(Form)
        self.lbl_auw_3.setGeometry(QtCore.QRect(690, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_3.setFont(font)
        self.lbl_auw_3.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_auw_3.setWordWrap(True)
        self.lbl_auw_3.setObjectName("lbl_auw_3")
        self.lbl_auw_4 = QtWidgets.QLabel(Form)
        self.lbl_auw_4.setGeometry(QtCore.QRect(690, 360, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_4.setFont(font)
        self.lbl_auw_4.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_auw_4.setWordWrap(True)
        self.lbl_auw_4.setObjectName("lbl_auw_4")
        self.lbl_auw_5 = QtWidgets.QLabel(Form)
        self.lbl_auw_5.setGeometry(QtCore.QRect(690, 470, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_5.setFont(font)
        self.lbl_auw_5.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_auw_5.setWordWrap(True)
        self.lbl_auw_5.setObjectName("lbl_auw_5")
        self.lbl_auw_6 = QtWidgets.QLabel(Form)
        self.lbl_auw_6.setGeometry(QtCore.QRect(690, 570, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_6.setFont(font)
        self.lbl_auw_6.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_auw_6.setWordWrap(True)
        self.lbl_auw_6.setObjectName("lbl_auw_6")
        self.lbl_auw_7 = QtWidgets.QLabel(Form)
        self.lbl_auw_7.setGeometry(QtCore.QRect(690, 670, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_auw_7.setFont(font)
        self.lbl_auw_7.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_auw_7.setWordWrap(True)
        self.lbl_auw_7.setObjectName("lbl_auw_7")
        self.lbl_inf_4 = QtWidgets.QLabel(Form)
        self.lbl_inf_4.setGeometry(QtCore.QRect(840, 570, 240, 80))
        self.lbl_inf_4.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_inf_4.setText("")
        self.lbl_inf_4.setObjectName("lbl_inf_4")
        self.lbl_inf_1 = QtWidgets.QLabel(Form)
        self.lbl_inf_1.setGeometry(QtCore.QRect(840, 250, 240, 81))
        self.lbl_inf_1.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_inf_1.setText("")
        self.lbl_inf_1.setObjectName("lbl_inf_1")
        self.lbl_inf_5 = QtWidgets.QLabel(Form)
        self.lbl_inf_5.setGeometry(QtCore.QRect(840, 670, 240, 80))
        self.lbl_inf_5.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_inf_5.setText("")
        self.lbl_inf_5.setObjectName("lbl_inf_5")
        self.lbl_inf_3 = QtWidgets.QLabel(Form)
        self.lbl_inf_3.setGeometry(QtCore.QRect(840, 470, 240, 80))
        self.lbl_inf_3.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_inf_3.setText("")
        self.lbl_inf_3.setObjectName("lbl_inf_3")
        self.lbl_inf_2 = QtWidgets.QLabel(Form)
        self.lbl_inf_2.setGeometry(QtCore.QRect(840, 360, 240, 80))
        self.lbl_inf_2.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_inf_2.setText("")
        self.lbl_inf_2.setObjectName("lbl_inf_2")
        self.lbl_axis = QtWidgets.QLabel(Form)
        self.lbl_axis.setGeometry(QtCore.QRect(840, 100, 221, 41))
        self.lbl_axis.setStyleSheet("background-color:#fff;\n"
"border-radius:10px;")
        self.lbl_axis.setText("")
        self.lbl_axis.setObjectName("lbl_axis")
        self.label_acc = QtWidgets.QLabel(Form)
        self.label_acc.setGeometry(QtCore.QRect(700, 100, 91, 41))
        self.label_acc.setStyleSheet("background-color:rgb(216, 231, 33);\n"
"border-radius:10px;")
        self.label_acc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_acc.setObjectName("label_acc")
        self.lbl_auw_X_value = QtWidgets.QLabel(Form)
        self.lbl_auw_X_value.setGeometry(QtCore.QRect(800, 160, 81, 31))
        self.lbl_auw_X_value.setStyleSheet("background-color:rgb(188, 231, 228);\n"
"border-radius:10px;")
        self.lbl_auw_X_value.setText("")
        self.lbl_auw_X_value.setObjectName("lbl_auw_X_value")
        self.lbl_auw_X = QtWidgets.QLabel(Form)
        self.lbl_auw_X.setGeometry(QtCore.QRect(700, 160, 71, 31))
        self.lbl_auw_X.setStyleSheet("background-color:rgb(191, 180, 180);\n"
"border-radius:10px;")
        self.lbl_auw_X.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_auw_X.setObjectName("lbl_auw_X")
        self.lbl_auw_Y_value = QtWidgets.QLabel(Form)
        self.lbl_auw_Y_value.setGeometry(QtCore.QRect(1010, 160, 81, 31))
        self.lbl_auw_Y_value.setStyleSheet("background-color:rgb(188, 231, 228);\n"
"border-radius:10px;")
        self.lbl_auw_Y_value.setText("")
        self.lbl_auw_Y_value.setObjectName("lbl_auw_Y_value")
        self.lbl_auw_Y = QtWidgets.QLabel(Form)
        self.lbl_auw_Y.setGeometry(QtCore.QRect(910, 160, 71, 31))
        self.lbl_auw_Y.setStyleSheet("background-color:rgb(191, 180, 180);\n"
"border-radius:10px;")
        self.lbl_auw_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_auw_Y.setObjectName("lbl_auw_Y")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AUTOMATION"))
        self.lbl_auw_02.setText(_translate("Form", "Webcam"))
        self.btn_auw_stop.setText(_translate("Form", "Stop"))
        self.btn_auw_back.setText(_translate("Form", "Back"))
        self.btn_auw_change.setText(_translate("Form", "Setup Systerm Funtion"))
        self.lbl_auw3.setText(_translate("Form", "Number of goods"))
        self.lbl_auw_01.setText(_translate("Form", "Automation"))
        self.btn_auw_continue.setText(_translate("Form", "Continue"))
        self.lbl_auw_3.setText(_translate("Form", "Information of goods"))
        self.lbl_auw_4.setText(_translate("Form", "Information of goods"))
        self.lbl_auw_5.setText(_translate("Form", "Information of goods"))
        self.lbl_auw_6.setText(_translate("Form", "Information of goods"))
        self.lbl_auw_7.setText(_translate("Form", "Information of goods"))
        self.label_acc.setText(_translate("Form", "Angle"))
        self.lbl_auw_X.setText(_translate("Form", "X"))
        self.lbl_auw_Y.setText(_translate("Form", "Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
