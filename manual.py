# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1211, 778)
        Form.setStyleSheet("background-color:rgb(235, 238, 255)")
        self.lbl_manual_02 = QtWidgets.QLabel(Form)
        self.lbl_manual_02.setGeometry(QtCore.QRect(30, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_02.setFont(font)
        self.lbl_manual_02.setStyleSheet("background-color:#fff;")
        self.lbl_manual_02.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_02.setObjectName("lbl_manual_02")
        self.btn_manual_set = QtWidgets.QPushButton(Form)
        self.btn_manual_set.setGeometry(QtCore.QRect(640, 70, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_set.setFont(font)
        self.btn_manual_set.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_set.setObjectName("btn_manual_set")
        self.cb_manual_motor = QtWidgets.QComboBox(Form)
        self.cb_manual_motor.setGeometry(QtCore.QRect(380, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_manual_motor.setFont(font)
        self.cb_manual_motor.setStyleSheet("background-color:#fff;")
        self.cb_manual_motor.setObjectName("cb_manual_motor")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.cb_manual_motor.addItem("")
        self.btn_manual_module_1 = QtWidgets.QPushButton(Form)
        self.btn_manual_module_1.setGeometry(QtCore.QRect(470, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_module_1.setFont(font)
        self.btn_manual_module_1.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_module_1.setObjectName("btn_manual_module_1")
        self.btn_manual_module_2 = QtWidgets.QPushButton(Form)
        self.btn_manual_module_2.setGeometry(QtCore.QRect(370, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_module_2.setFont(font)
        self.btn_manual_module_2.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_module_2.setObjectName("btn_manual_module_2")
        self.btn_manual_module_3 = QtWidgets.QPushButton(Form)
        self.btn_manual_module_3.setGeometry(QtCore.QRect(570, 290, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_module_3.setFont(font)
        self.btn_manual_module_3.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_module_3.setObjectName("btn_manual_module_3")
        self.lbl_manual_diretion = QtWidgets.QLabel(Form)
        self.lbl_manual_diretion.setGeometry(QtCore.QRect(380, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_diretion.setFont(font)
        self.lbl_manual_diretion.setStyleSheet("background-color:#fff;\n"
"border-radius:16px;\n"
"")
        self.lbl_manual_diretion.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_diretion.setObjectName("lbl_manual_diretion")
        self.lbl_manual_cam = QtWidgets.QLabel(Form)
        self.lbl_manual_cam.setGeometry(QtCore.QRect(30, 180, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_cam.setFont(font)
        self.lbl_manual_cam.setStyleSheet("background-color:#fff;\n"
"border-radius:16px;\n"
"")
        self.lbl_manual_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_cam.setObjectName("lbl_manual_cam")
        self.lbl_manual_number = QtWidgets.QLabel(Form)
        self.lbl_manual_number.setGeometry(QtCore.QRect(40, 490, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_number.setFont(font)
        self.lbl_manual_number.setStyleSheet("background-color:rgb(91, 225, 214);\n"
"border-radius:16px;\n"
"")
        self.lbl_manual_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_number.setWordWrap(True)
        self.lbl_manual_number.setObjectName("lbl_manual_number")
        self.lbl_manual_01 = QtWidgets.QLabel(Form)
        self.lbl_manual_01.setGeometry(QtCore.QRect(10, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_manual_01.setFont(font)
        self.lbl_manual_01.setStyleSheet("background-color:rgb(200, 255, 176);")
        self.lbl_manual_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_01.setObjectName("lbl_manual_01")
        self.btn_manual_back = QtWidgets.QPushButton(Form)
        self.btn_manual_back.setGeometry(QtCore.QRect(1030, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_back.setFont(font)
        self.btn_manual_back.setStyleSheet("background-color:rgb(85, 255, 127)")
        self.btn_manual_back.setObjectName("btn_manual_back")
        self.plt_manual_speed = QtWidgets.QPlainTextEdit(Form)
        self.plt_manual_speed.setGeometry(QtCore.QRect(520, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plt_manual_speed.setFont(font)
        self.plt_manual_speed.setStyleSheet("background-color:#fff;")
        self.plt_manual_speed.setPlainText("")
        self.plt_manual_speed.setObjectName("plt_manual_speed")
        self.tbl_manual_quantity = QtWidgets.QTableWidget(Form)
        self.tbl_manual_quantity.setGeometry(QtCore.QRect(150, 490, 421, 271))
        self.tbl_manual_quantity.setStyleSheet("background-color:rgb(251, 255, 205)")
        self.tbl_manual_quantity.setRowCount(5)
        self.tbl_manual_quantity.setColumnCount(4)
        self.tbl_manual_quantity.setObjectName("tbl_manual_quantity")
        self.lbl_manual_6 = QtWidgets.QLabel(Form)
        self.lbl_manual_6.setGeometry(QtCore.QRect(720, 640, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_6.setFont(font)
        self.lbl_manual_6.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_manual_6.setWordWrap(True)
        self.lbl_manual_6.setObjectName("lbl_manual_6")
        self.lbl_manual_4 = QtWidgets.QLabel(Form)
        self.lbl_manual_4.setGeometry(QtCore.QRect(720, 430, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_4.setFont(font)
        self.lbl_manual_4.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_manual_4.setWordWrap(True)
        self.lbl_manual_4.setObjectName("lbl_manual_4")
        self.lbl_manual_2 = QtWidgets.QLabel(Form)
        self.lbl_manual_2.setGeometry(QtCore.QRect(720, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_2.setFont(font)
        self.lbl_manual_2.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_manual_2.setWordWrap(True)
        self.lbl_manual_2.setObjectName("lbl_manual_2")
        self.lbl_manual_3 = QtWidgets.QLabel(Form)
        self.lbl_manual_3.setGeometry(QtCore.QRect(720, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_3.setFont(font)
        self.lbl_manual_3.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_manual_3.setWordWrap(True)
        self.lbl_manual_3.setObjectName("lbl_manual_3")
        self.lbl_manual_5 = QtWidgets.QLabel(Form)
        self.lbl_manual_5.setGeometry(QtCore.QRect(720, 530, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_manual_5.setFont(font)
        self.lbl_manual_5.setStyleSheet("background-color:rgb(228, 191, 191);\n"
"border-radius:10px;")
        self.lbl_manual_5.setWordWrap(True)
        self.lbl_manual_5.setObjectName("lbl_manual_5")
        self.lbl_img = QtWidgets.QLabel(Form)
        self.lbl_img.setGeometry(QtCore.QRect(30, 230, 320, 240))
        self.lbl_img.setStyleSheet("background-color:#fff")
        self.lbl_img.setText("")
        self.lbl_img.setObjectName("lbl_img")
        self.cbox_manual_function = QtWidgets.QComboBox(Form)
        self.cbox_manual_function.setGeometry(QtCore.QRect(170, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbox_manual_function.setFont(font)
        self.cbox_manual_function.setStyleSheet("background-color:#fff;")
        self.cbox_manual_function.setObjectName("cbox_manual_function")
        self.cbox_manual_function.addItem("")
        self.cbox_manual_function.addItem("")
        self.cb_manual_module = QtWidgets.QComboBox(Form)
        self.cb_manual_module.setGeometry(QtCore.QRect(380, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_manual_module.setFont(font)
        self.cb_manual_module.setStyleSheet("background-color:#fff;")
        self.cb_manual_module.setObjectName("cb_manual_module")
        self.cb_manual_module.addItem("")
        self.cb_manual_module.addItem("")
        self.cb_manual_module.addItem("")
        self.cb_manual_module.addItem("")
        self.btn_manual_start = QtWidgets.QPushButton(Form)
        self.btn_manual_start.setGeometry(QtCore.QRect(210, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_start.setFont(font)
        self.btn_manual_start.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_start.setObjectName("btn_manual_start")
        self.btn_manual_stop = QtWidgets.QPushButton(Form)
        self.btn_manual_stop.setGeometry(QtCore.QRect(460, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_stop.setFont(font)
        self.btn_manual_stop.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_stop.setObjectName("btn_manual_stop")
        self.btn_manual_continue = QtWidgets.QPushButton(Form)
        self.btn_manual_continue.setGeometry(QtCore.QRect(450, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_manual_continue.setFont(font)
        self.btn_manual_continue.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:10px;")
        self.btn_manual_continue.setObjectName("btn_manual_continue")
        self.lbl_manual_inf_1 = QtWidgets.QLabel(Form)
        self.lbl_manual_inf_1.setGeometry(QtCore.QRect(880, 210, 240, 80))
        self.lbl_manual_inf_1.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_manual_inf_1.setText("")
        self.lbl_manual_inf_1.setObjectName("lbl_manual_inf_1")
        self.lbl_manual_inf_2 = QtWidgets.QLabel(Form)
        self.lbl_manual_inf_2.setGeometry(QtCore.QRect(880, 320, 240, 80))
        self.lbl_manual_inf_2.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_manual_inf_2.setText("")
        self.lbl_manual_inf_2.setObjectName("lbl_manual_inf_2")
        self.lbl_manual_inf_3 = QtWidgets.QLabel(Form)
        self.lbl_manual_inf_3.setGeometry(QtCore.QRect(880, 430, 240, 80))
        self.lbl_manual_inf_3.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_manual_inf_3.setText("")
        self.lbl_manual_inf_3.setObjectName("lbl_manual_inf_3")
        self.lbl_manual_inf_4 = QtWidgets.QLabel(Form)
        self.lbl_manual_inf_4.setGeometry(QtCore.QRect(880, 530, 240, 80))
        self.lbl_manual_inf_4.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_manual_inf_4.setText("")
        self.lbl_manual_inf_4.setObjectName("lbl_manual_inf_4")
        self.lbl_manual_inf_5 = QtWidgets.QLabel(Form)
        self.lbl_manual_inf_5.setGeometry(QtCore.QRect(880, 640, 240, 80))
        self.lbl_manual_inf_5.setStyleSheet("background-color:rgb(188, 221, 244);\n"
"border-radius:10px;")
        self.lbl_manual_inf_5.setText("")
        self.lbl_manual_inf_5.setObjectName("lbl_manual_inf_5")
        self.label_acc = QtWidgets.QLabel(Form)
        self.label_acc.setGeometry(QtCore.QRect(790, 80, 91, 41))
        self.label_acc.setStyleSheet("background-color:rgb(216, 231, 33);")
        self.label_acc.setObjectName("label_acc")
        self.lbl_axis = QtWidgets.QLabel(Form)
        self.lbl_axis.setGeometry(QtCore.QRect(920, 80, 221, 41))
        self.lbl_axis.setStyleSheet("background-color:#fff;")
        self.lbl_axis.setText("")
        self.lbl_axis.setObjectName("lbl_axis")
        self.lbl_manual_x_value = QtWidgets.QLabel(Form)
        self.lbl_manual_x_value.setGeometry(QtCore.QRect(890, 140, 81, 31))
        self.lbl_manual_x_value.setStyleSheet("background-color:rgb(188, 231, 228);\n"
"border-radius:10px;")
        self.lbl_manual_x_value.setText("")
        self.lbl_manual_x_value.setObjectName("lbl_manual_x_value")
        self.lbl_manual_y_value = QtWidgets.QLabel(Form)
        self.lbl_manual_y_value.setGeometry(QtCore.QRect(1100, 140, 81, 31))
        self.lbl_manual_y_value.setStyleSheet("background-color:rgb(188, 231, 228);\n"
"border-radius:10px;")
        self.lbl_manual_y_value.setText("")
        self.lbl_manual_y_value.setObjectName("lbl_manual_y_value")
        self.lbl_manual_x = QtWidgets.QLabel(Form)
        self.lbl_manual_x.setGeometry(QtCore.QRect(790, 140, 71, 31))
        self.lbl_manual_x.setStyleSheet("background-color:rgb(191, 180, 180);\n"
"border-radius:10px;")
        self.lbl_manual_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_x.setObjectName("lbl_manual_x")
        self.lbl_manual_y = QtWidgets.QLabel(Form)
        self.lbl_manual_y.setGeometry(QtCore.QRect(1000, 140, 71, 31))
        self.lbl_manual_y.setStyleSheet("background-color:rgb(191, 180, 180);\n"
"border-radius:10px;")
        self.lbl_manual_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_manual_y.setObjectName("lbl_manual_y")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_manual_02.setText(_translate("Form", "Chang speed"))
        self.btn_manual_set.setText(_translate("Form", "Set"))
        self.cb_manual_motor.setItemText(0, _translate("Form", "Motor 1"))
        self.cb_manual_motor.setItemText(1, _translate("Form", "Motor 2"))
        self.cb_manual_motor.setItemText(2, _translate("Form", "Motor 3"))
        self.cb_manual_motor.setItemText(3, _translate("Form", "Motor 4"))
        self.cb_manual_motor.setItemText(4, _translate("Form", "Motor 5"))
        self.cb_manual_motor.setItemText(5, _translate("Form", "Motor 6"))
        self.cb_manual_motor.setItemText(6, _translate("Form", "Motor 7"))
        self.cb_manual_motor.setItemText(7, _translate("Form", "Motor 8"))
        self.cb_manual_motor.setItemText(8, _translate("Form", "Motor 9"))
        self.cb_manual_motor.setItemText(9, _translate("Form", "Motor 10"))
        self.btn_manual_module_1.setText(_translate("Form", "Output module 1"))
        self.btn_manual_module_2.setText(_translate("Form", "Output module 2"))
        self.btn_manual_module_3.setText(_translate("Form", "Output module 3"))
        self.lbl_manual_diretion.setText(_translate("Form", "Direction"))
        self.lbl_manual_cam.setText(_translate("Form", "Cam"))
        self.lbl_manual_number.setText(_translate("Form", "Number of goods"))
        self.lbl_manual_01.setText(_translate("Form", "Manual"))
        self.btn_manual_back.setText(_translate("Form", "Chuyển chế độ"))
        self.lbl_manual_6.setText(_translate("Form", "Information of goods"))
        self.lbl_manual_4.setText(_translate("Form", "Information of goods"))
        self.lbl_manual_2.setText(_translate("Form", "Information of goods"))
        self.lbl_manual_3.setText(_translate("Form", "Information of goods"))
        self.lbl_manual_5.setText(_translate("Form", "Information of goods"))
        self.cbox_manual_function.setItemText(0, _translate("Form", "Theo module"))
        self.cbox_manual_function.setItemText(1, _translate("Form", "Theo từng động cơ"))
        self.cb_manual_module.setItemText(0, _translate("Form", "Module 1"))
        self.cb_manual_module.setItemText(1, _translate("Form", "Module 2"))
        self.cb_manual_module.setItemText(2, _translate("Form", "Module 3"))
        self.cb_manual_module.setItemText(3, _translate("Form", "Module 4"))
        self.btn_manual_start.setText(_translate("Form", "Start"))
        self.btn_manual_stop.setText(_translate("Form", "Stop"))
        self.btn_manual_continue.setText(_translate("Form", "Continue"))
        self.label_acc.setText(_translate("Form", "Angle"))
        self.lbl_manual_x.setText(_translate("Form", "X"))
        self.lbl_manual_y.setText(_translate("Form", "Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
