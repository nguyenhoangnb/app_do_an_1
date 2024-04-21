# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(930, 559)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setAccessibleDescription("")
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(225, 254, 255)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_pro_manual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pro_manual.setGeometry(QtCore.QRect(530, 270, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_pro_manual.setFont(font)
        self.btn_pro_manual.setStyleSheet("background-color:rgb(255, 170, 0);\n"
"border:1px solid #333;\n"
"border-radius:30px;")
        self.btn_pro_manual.setObjectName("btn_pro_manual")
        self.btn_pro_auto = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pro_auto.setGeometry(QtCore.QRect(220, 270, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_pro_auto.setFont(font)
        self.btn_pro_auto.setStyleSheet("background-color:rgb(255, 170, 0);\n"
"border:1px solid #333;\n"
"border-radius:30px;")
        self.btn_pro_auto.setObjectName("btn_pro_auto")
        self.lbl_pro_01 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pro_01.setGeometry(QtCore.QRect(90, 40, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_pro_01.setFont(font)
        self.lbl_pro_01.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid #333; \n"
"border-radius: 10px;")
        self.lbl_pro_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pro_01.setObjectName("lbl_pro_01")
        self.lbl_imple = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imple.setGeometry(QtCore.QRect(540, 110, 381, 41))
        self.lbl_imple.setAutoFillBackground(False)
        self.lbl_imple.setStyleSheet("background-color:rgb(238, 232, 159);\n"
"border: 1px solid;\n"
"border-radius:10px;")
        self.lbl_imple.setWordWrap(True)
        self.lbl_imple.setObjectName("lbl_imple")
        self.lb_function = QtWidgets.QLabel(self.centralwidget)
        self.lb_function.setGeometry(QtCore.QRect(360, 180, 211, 51))
        self.lb_function.setStyleSheet("background-color:rgb(238, 146, 117);\n"
"font: 22pt \"Ubuntu\";\n"
"border-radius: 10px;")
        self.lb_function.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_function.setObjectName("lb_function")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_pro_manual.setText(_translate("MainWindow", "Manual"))
        self.btn_pro_auto.setText(_translate("MainWindow", "Automation"))
        self.lbl_pro_01.setText(_translate("MainWindow", "Classification and sorting system for goods using omni wheels"))
        self.lbl_imple.setText(_translate("MainWindow", "Implemented by Dr. Le Xuan Luc and the students of K66Robot"))
        self.lb_function.setText(_translate("MainWindow", "Function"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
