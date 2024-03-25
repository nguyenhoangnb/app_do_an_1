from handle import autoHandle
from handle import programHandle
from handle import autoworkHandle
from handle import byhandworkHandle
from pysql import *
import re
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox
import mysql.connector as con

speed_dc = {
    "Động cơ 1":0,
    "Động cơ 2":0,
    "Động cơ 3":0,
    "Động cơ 4":0,
    "Động cơ 5":0,
    "Động cơ 6":0,
    "Động cơ 7":0,
    "Động cơ 8":0,
    "Động cơ 9":0,
    "Động cơ 10":0,
    "Động cơ 11":0,
    "Động cơ 12":0,
    
}

class UI():
    def __init__(self):
        
        self.speed_dc = speed_dc
        self.speed_dc_pred = self.speed_dc
        
        self.programUi = QMainWindow()
        self.programHandle = programHandle(self.programUi)
        self.programHandle.btn_pro_auto.clicked.connect(lambda:self.automation())
        self.programHandle.btn_pr_byhand.clicked.connect(lambda:self.byhand())
        
        self.autoUI = QMainWindow()
        self.autoHandle = autoHandle(self.autoUI)
        self.autoHandle.btn_auto_start.clicked.connect(lambda:self.startauto())
        self.autoHandle.btn_auto_back.clicked.connect(lambda:self.back_to_main())
        self.autoHandle.btn_auto_set.clicked.connect(lambda:self.set_speed())
        
        self.autoworkUI = QMainWindow()
        self.autoworkHandle = autoworkHandle(self.autoworkUI)
        self.autoworkHandle.btn_auw_stop.clicked.connect(lambda: self.stop_auto())
        self.autoworkHandle.btn_auw_back.clicked.connect(lambda: self.back_auto_work())
        self.autoworkHandle.btn_auw_change.clicked.connect(lambda: self.back_to_main())
        self.autoworkHandle.btn_auw_continue.hide()
        self.autoworkHandle.btn_auw_continue.clicked.connect(lambda: self.continue_auto())
        
        self.byhandworkUI = QMainWindow()
        self.byhanworkHandle = byhandworkHandle(self.byhandworkUI)
        self.byhanworkHandle.btn_byh_back.clicked.connect(lambda:self.back_to_main())
        self.byhanworkHandle.btn_byh_set.clicked.connect(lambda: self.set_speed_byh())
        
        self.programUi.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_auto())
        self.timer.timeout.connect(lambda:self.insert_table_byhand())
        self.timer.start(10)

    
    def automation(self):
        self.programUi.hide()
        self.autoUI.show()
    
    def startauto(self):
        self.autoUI.hide()
        self.autoworkUI.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_auto())
        self.timer.start(10)
    
    def back_to_main(self):
        self.autoUI.hide()
        self.autoworkUI.hide()
        self.byhandworkUI.hide()
        self.programUi.show()
    
    def set_speed(self):
        pass
    
    def stop_auto(self):
        self.speed_dc_pred = self.speed_dc
        self.autoworkHandle.btn_auw_stop.hide()
        self.autoworkHandle.btn_auw_continue.show()
        for x in self.speed_dc:
            self.speed_dc[x] = 0
    def continue_auto(self):
        self.speed_dc = self.speed_dc_pred
        self.autoworkHandle.btn_auw_stop.show()
        self.autoworkHandle.btn_auw_continue.hide()
        
            
    def back_auto_work(self):
        self.autoworkUI.hide()
        self.autoUI.show()
    
    def byhand(self):
        self.programUi.hide()
        self.byhandworkUI.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_byhand())
        self.timer.start(10)
        
    def set_speed_byh(self):
        dc = self.byhanworkHandle.plainTextEdit.toPlainText()
        idx = self.byhanworkHandle.comboBox.currentText()
        if (not self.kiem_tra(dc)):
            print(dc)
            self.byhanworkHandle.plainTextEdit.setPlainText("0")
          
        speed_dc[idx] = int(self.byhanworkHandle.plainTextEdit.toPlainText())
        print(speed_dc)
    
    def insert_table_auto(self):
        mydb = MY_DB()
        mydb.connect("data.db")
        self.autoworkHandle.tbl_quantity.setRowCount(0)
        self.result = mydb.select_all("products")
        label = mydb.get_table_columns("products") 
        self.autoworkHandle.tbl_quantity.setHorizontalHeaderLabels(label)
        for row_num, row_data in enumerate(self.result):
            self.autoworkHandle.tbl_quantity.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.autoworkHandle.tbl_quantity.setItem(row_num, col_num, QTableWidgetItem(str(col_data))) 
        mydb.close()
    def insert_table_byhand(self):
        mydb = MY_DB()
        mydb.connect("data.db")
        self.byhanworkHandle.tbl_quantity.setRowCount(0)
        self.result = mydb.select_all("products")
        label = mydb.get_table_columns("products") 
        self.byhanworkHandle.tbl_quantity.setHorizontalHeaderLabels(label)
        for row_num, row_data in enumerate(self.result):
            self.byhanworkHandle.tbl_quantity.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.byhanworkHandle.tbl_quantity.setItem(row_num, col_num, QTableWidgetItem(str(col_data))) 
        mydb.close()
    def kiem_tra(self,xau):
        return bool(re.match(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', xau))
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    
    app.exec_()