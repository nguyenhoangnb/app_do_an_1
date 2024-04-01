from handle import autoHandle
from handle import programHandle
from handle import autoworkHandle
from handle import byhandworkHandle
from pysql import *
import re

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox
import imutils
import numpy as np

import mysql.connector as con
from PyQt5.QtGui import QImage, QPixmap
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Int16

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

speed_module = {
    "Module 1":0,
    "Module 2":0,
    "Module 3":0,
    "Module 4":0
}

def detect_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)  # Điều chỉnh độ chính xác

    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = float(w) / h

    if len(approx) == 3:
        return "tamgiac"
    elif len(approx) == 4:
        if 0.95 <= aspect_ratio <= 1.05:
            return "vuong"
        else:
            return "chu nhat"
    else:
        return "tron"

class UI():
    def __init__(self):
        
        self.speed_dc = speed_dc
        self.speed_dc_pred = self.speed_dc
        #program UI
        self.programUi = QMainWindow()
        self.programHandle = programHandle(self.programUi)
        self.programHandle.btn_pro_auto.clicked.connect(lambda:self.automation())
        self.programHandle.btn_pr_byhand.clicked.connect(lambda:self.byhand())
        # Auto Ui
        self.autoUI = QMainWindow()
        self.autoHandle = autoHandle(self.autoUI)
        self.autoHandle.btn_auto_start.clicked.connect(lambda:self.startauto())
        self.autoHandle.btn_auto_back.clicked.connect(lambda:self.back_to_main())
        self.autoHandle.btn_auto_set.clicked.connect(lambda:self.set_speed_auto())
        #Autowork UI
        self.autoworkUI = QMainWindow()
        self.autoworkHandle = autoworkHandle(self.autoworkUI)
        self.autoworkHandle.btn_auw_stop.clicked.connect(lambda: self.stop_auto())
        self.autoworkHandle.btn_auw_back.clicked.connect(lambda: self.back_auto_work())
        self.autoworkHandle.btn_auw_change.clicked.connect(lambda: self.back_to_main())
        self.autoworkHandle.btn_auw_continue.hide()
        self.autoworkHandle.btn_auw_continue.clicked.connect(lambda: self.continue_auto())
        #ByhandWork UI
        self.byhandworkUI = QMainWindow()
        self.byhanworkHandle = byhandworkHandle(self.byhandworkUI)
        self.byhanworkHandle.btn_byh_back.clicked.connect(lambda:self.back_to_main())
        self.byhanworkHandle.btn_byh_set.clicked.connect(lambda: self.set_speed_byh())
        #Topic name
        self.topic_img = "image_raw"
        self.topic_speed_auto = "speed_auto"
        self.bridge = CvBridge()
        
        self.idx = 0
        self.programUi.show()
        self.timer = QTimer()
        # self.timer.timeout.connect(lambda:self.insert_table_auto())
        # self.timer.timeout.connect(lambda:self.insert_table_byhand())
        # self.timer.start(10)

 
    # Enable UI
    # def enable(self, state):
    #     if state == 1:
    #         self.autoUI.setEnabled(True)
    #         self.autoworkUI.setEnabled(False)
    #         self.programUi.setEnabled(False)
    #         self.byhandworkUI.setEnabled(False)
    #     if state == 2:
    #         self.autoUI.setEnabled(False)
    #         self.autoworkUI.setEnabled(True)
    #         self.programUi.setEnabled(False)
    #         self.byhandworkUI.setEnabled(False)
    #     if state == 3:
    #         self.autoUI.setEnabled(False)
    #         self.autoworkUI.setEnabled(False)
    #         self.programUi.setEnabled(True)
    #         self.byhandworkUI.setEnabled(False)
    #     if state == 4:
    #         self.autoUI.setEnabled(False)
    #         self.autoworkUI.setEnabled(False)
    #         self.programUi.setEnabled(False)
    #         self.byhandworkUI.setEnabled(True)
    # Change between modes
    def automation(self):
        self.programUi.hide()
        self.autoUI.show()
        
    def startauto(self):
        self.autoUI.hide()
        self.autoworkUI.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_auto())
        self.timer.start(10)  
        rospy.init_node("img_node", anonymous=True)
        
        self.sub = rospy.Subscriber(
            self.topic_img,
            Image,
            self.sub_callback
        )

        self.timer.timeout.connect(self.update_image)
        self.timer.start(100)  
        
        
    
    def back_to_main(self):
        self.autoUI.hide()
        self.autoworkUI.hide()
        self.byhandworkUI.hide()
        self.programUi.show()
    
    def create_combo_box_byh(self):
        pass    
    
    #set speed auto
    def set_speed_auto(self):
        text = self.autoHandle.cb_auto_speed.currentText()
        rospy.init_node("speed_auto", anonymous=True)
        self.pub_speed_auto = rospy.Publisher(
            self.topic_speed_auto,
            Int16,
            queue_size=10
        )
        rate = rospy.Rate(1)
        mode = 0
        if text == "Nhanh":
            mode = 1
        if text == "Thường":
            mode = 2
        if text == "Chậm":
            mode = 3
        self.pub_speed_auto.publish(mode)
        
        # try:
        #     while not rospy.is_shutdown():
        #         self.pub_speed_auto.publish(mode)
        #         rate.sleep()
        # except rospy.ROSInterruptException:
        #     rospy.signal_shutdown("ROSInterruptExeption")

    #Set speed byhand
    def set_speed_byhand(self):
        
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
        rospy.init_node("img_node", anonymous=True)
        
        self.sub = rospy.Subscriber(
            self.topic_img,
            Image,
            self.sub_callback_byh
        )

        self.timer.timeout.connect(self.update_image)
        self.timer.start(100)  
        self.byhanworkHandle.cbox_fun.currentIndexChanged.connect(self.byhand_change)
        self.byhanworkHandle.btn_byh_set.clicked.connect(lambda: self.set_speed_byh(self.idx))
    
    def byhand_change(self, idx):
        print(idx)
        if idx == 0:
            self.byhanworkHandle.cb_box_module.show()
            self.byhanworkHandle.cb_motor.hide()
        elif idx == 1:
            self.byhanworkHandle.cb_box_module.hide()
            self.byhanworkHandle.cb_motor.show()
        self.idx = idx
        
    def set_speed_byh(self, current_idx):
        if current_idx == 1:
            dc = self.byhanworkHandle.plt_speed.toPlainText()
            idx = self.byhanworkHandle.cb_motor.currentText()
            if (not self.kiem_tra(dc)):
                print(dc)
                self.byhanworkHandle.plt_speed.setPlainText("0")
            else:
                speed_dc[idx] = int(self.byhanworkHandle.plt_speed.toPlainText())
            print(speed_dc)
        elif current_idx == 0:
            mod_speed = self.byhanworkHandle.plt_speed.toPlainText()
            idx_mod = self.byhanworkHandle.cb_box_module.currentText()
            print(idx_mod)
            if not self.kiem_tra(mod_speed):
                self.byhanworkHandle.plt_speed.setPlainText("0")
            else:
                speed_module[idx_mod] = int(self.byhanworkHandle.plt_speed.toPlainText())
            print(mod_speed)
        
    #insert table
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
    
    def sub_callback(self, image):
        cv_image = self.bridge.imgmsg_to_cv2(image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = cv_image.shape
        bytes_per_line = ch * w
        
        cv_image = self.setImage(cv_image)
        
        qt_img = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.autoworkHandle.lbl_img.setPixmap(pixmap.scaled(self.autoworkHandle.lbl_img.size(), Qt.KeepAspectRatio))
    def sub_callback_byh(self, image):
        cv_image = self.bridge.imgmsg_to_cv2(image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = cv_image.shape
        bytes_per_line = ch * w
        
        cv_image = self.setImage(cv_image)
        
        qt_img = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.byhanworkHandle.lbl_img.setPixmap(pixmap.scaled(self.byhanworkHandle.lbl_img.size(), Qt.KeepAspectRatio))


    def update_image(self):
        
        pass
    # @staticmethod
    def setImage(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_Yellow = np.array([25,70,125])
        upper_Yellow = np.array([35,255,255])

        lower_Green = np.array([65, 60, 60])
        upper_Green = np.array([80, 255, 255])

        lower_Red = np.array([0,70,150])
        upper_Red = np.array([15,255,255])

        lower_Blue = np.array([90,60,70])
        upper_Blue = np.array([114,255,255])

        lower_Purple = np.array([[125, 30, 50]])
        upper_Purple = np.array([140, 255, 255])

        mask1 = cv2.inRange(hsv, lower_Yellow, upper_Yellow)
        mask2 = cv2.inRange(hsv, lower_Green, upper_Green)
        mask3 = cv2.inRange(hsv, lower_Red, upper_Red)
        mask4 = cv2.inRange(hsv, lower_Blue, upper_Blue)
        mask5 = cv2.inRange(hsv, lower_Purple, upper_Purple)

        cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts1 = imutils.grab_contours(cnts1)

        cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts2 = imutils.grab_contours(cnts2)

        cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts3 = imutils.grab_contours(cnts3)

        cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts4 = imutils.grab_contours(cnts4)

        cnts5 = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts5 = imutils.grab_contours(cnts5)

        a = 0
        for c in cnts1:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                a = 1
                shape = detect_shape(c)
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, shape + " (Yellow)", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("vat the mau vang")

        for c in cnts2:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                a = 2
                shape = detect_shape(c)
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, shape + " (Green)", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("vat the mau xanh la cay")

        for c in cnts3:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                a = 3
                shape = detect_shape(c)
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, shape + " (Red)", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("vat the mau do")

        for c in cnts4:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                a = 4
                shape = detect_shape(c)
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, shape + " (Blue)", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("vat the mau xanh nuoc bien")

        for c in cnts5:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                a = 5
                shape = detect_shape(c)
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, shape + " (Purple)", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print("vat the mau tim")

        return frame
    
    
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    
    app.exec_()