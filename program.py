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
        MainWindow.resize(645, 520)
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
        self.btn_pr_byhand = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pr_byhand.setGeometry(QtCore.QRect(350, 150, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_pr_byhand.setFont(font)
        self.btn_pr_byhand.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.btn_pr_byhand.setObjectName("btn_pr_byhand")
        self.btn_pro_auto = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pro_auto.setGeometry(QtCore.QRect(90, 150, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_pro_auto.setFont(font)
        self.btn_pro_auto.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.btn_pro_auto.setObjectName("btn_pro_auto")
        self.lbl_pro_01 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pro_01.setGeometry(QtCore.QRect(140, 40, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_pro_01.setFont(font)
        self.lbl_pro_01.setStyleSheet("background-color: rgb(170, 255, 127)")
        self.lbl_pro_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pro_01.setObjectName("lbl_pro_01")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
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
        self.btn_pr_byhand.setText(_translate("MainWindow", "Điều khiển thủ công"))
        self.btn_pro_auto.setText(_translate("MainWindow", "Điều khiển tự động"))
        self.lbl_pro_01.setText(_translate("MainWindow", "Chức năng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
