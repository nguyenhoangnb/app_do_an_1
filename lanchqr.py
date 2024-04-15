from handle import autoHandle
from handle import programHandle
from handle import autoworkHandle
from handle import byhandworkHandle
from pysql import *
import re
import json
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox
import imutils
import math
import numpy as np

import mysql.connector as con
from PyQt5.QtGui import QImage, QPixmap
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, Imu
from std_msgs.msg import Int16, String

speed_dc = {
    "Motor 1":0,
    "Motor 2":0,
    "Motor 3":0,
    "Motor 4":0,
    "Motor 5":0,
    "Motor 6":0,
    "Motor 7":0,
    "Motor 8":0,
    "Motor 9":0,
    "Motor 10":0,
    "Motor 11":0,
    "Motor 12":0,
    
}

speed_module = {
    "Module 1":0,
    "Module 2":0,
    "Module 3":0,
    "Module 4":0
}


pre_data = {
    "key1":"asdsa",
    "key2":"asdsa",
    "key3":"asdsa",
    "key4":"asdsa",
    "key5":"asdssa"
}

data = {
    "key1":"asdsa",
    "key2":"asdsa",
    "key3":"asdsa",
    "key4":"asdsa",
    "key5":"asdsa"
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
        
        self.idx = 0
        self.speed_dc = speed_dc
        self.speed_dc_pred = self.speed_dc
        self.data = data
        self.prev_data = pre_data
        
        self.speed_module = speed_module
        self.speed_module_pred = speed_module
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
        self.byhanworkHandle.btn_byh_set.clicked.connect(lambda: self.set_speed_byh(self.idx))
        self.byhanworkHandle.btn_byh_start.clicked.connect(lambda: self.start_byhand())
        self.byhanworkHandle.btn_byh_stop.clicked.connect(lambda: self.stop_byhand())
        self.byhanworkHandle.btn_byh_continue.clicked.connect(lambda: self.continue_byhand())
        self.byhanworkHandle.btn_byh_left.clicked.connect(lambda: self.dic_left())
        self.byhanworkHandle.btn_byh_right.clicked.connect(lambda: self.dic_right())
        self.byhanworkHandle.btn_byh_up.clicked.connect(lambda: self.dic_up())
        self.byhanworkHandle.btn_byh_down.clicked.connect(lambda: self.dic_dobtn_byh_down())
        
        #Topic name
        self.topic_img = "image_raw"
        self.topic_speed_auto = "speed_auto"
        self.topic_speed_by_module = "speed_module"
        self.topic_speed_by_motor = "speed_motor"
        self.topic_direction = "direction"
        self.topic_imu = "handsfree/imu"
        self.bridge = CvBridge()
        
        self.programUi.show()
        self.timer = QTimer()
        # self.timer.timeout.connect(lambda:self.insert_table_auto())
        # self.timer.timeout.connect(lambda:self.insert_table_byhand())
        # self.timer.start(10)
        self.pub_speed_motor = rospy.Publisher(
            self.topic_speed_by_motor,
            String,
            queue_size=20
        )
        self.pub_speed_module = rospy.Publisher(
            self.topic_speed_by_module,
            String,
            queue_size=10
        )
        self.pub_direction = rospy.Publisher(
            self.topic_direction,
            String,
            queue_size=10
        )
        rospy.init_node("img_node", anonymous=True)

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
        # self.timer.start(10)  
        
        self.sub = rospy.Subscriber(
            self.topic_img,
            Image,
            self.sub_callback
        )
        self.sub_imu = rospy.Subscriber(
            self.topic_imu,
            Imu,
            lambda msg: self.imuCallback(msg,1)
        )
        
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000)  
        
        
    
    def back_to_main(self):
        self.autoUI.hide()
        self.autoworkUI.hide()
        self.byhandworkUI.hide()
        self.programUi.show()
    
   
    
    #set speed auto
    def set_speed_auto(self):
        text = self.autoHandle.cb_auto_speed.currentText()
        # rospy.init_node("speed_auto", anonymous=True)
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
        self.byhanworkHandle.btn_byh_continue.hide()
        
        self.sub = rospy.Subscriber(
            self.topic_img,
            Image,
            self.sub_callback_byh
        )
        self.sub_imu = rospy.Subscriber(
            self.topic_imu,
            Imu,
            lambda msg: self.imuCallback(msg,2)
        )
        # rospy.Timer(rospy.Duration(1), self.update_image)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000)  
        self.byhanworkHandle.cbox_fun.currentIndexChanged.connect(self.byhand_change)
        # self.byhanworkHandle.btn_byh_set.clicked.connect(lambda: self.set_speed_byh(self.idx))
        
    
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
        # rospy.init_node("ros_speed", anonymous=True)
        
        if current_idx == 1:
            
            dc = self.byhanworkHandle.plt_speed.toPlainText()
            idx = self.byhanworkHandle.cb_motor.currentText()
            if (not self.kiem_tra(dc)):
                print(dc)
                self.byhanworkHandle.plt_speed.setPlainText("0")
            else:
                self.speed_dc[idx] = int(self.byhanworkHandle.plt_speed.toPlainText())
                
            print(self.speed_dc)
        elif current_idx == 0:
            mod_speed = self.byhanworkHandle.plt_speed.toPlainText()
            idx_mod = self.byhanworkHandle.cb_box_module.currentText()
            print(idx_mod)
            if not self.kiem_tra(mod_speed):
                self.byhanworkHandle.plt_speed.setPlainText("0")
            else:
                self.speed_module[idx_mod] = int(self.byhanworkHandle.plt_speed.toPlainText())
            print(mod_speed)
            
    def start_byhand(self):
        self.byhanworkHandle.btn_byh_continue.hide()
        self.byhanworkHandle.btn_byh_stop.show()

        if self.idx == 0:
            json_data = json.dumps(self.speed_module, ensure_ascii=False)
            self.pub_speed_module.publish(json_data)
        elif self.idx == 1:
            json_data = json.dumps(self.speed_dc, ensure_ascii=False)
            self.pub_speed_motor.publish(json_data)

    def stop_byhand(self):
        self.byhanworkHandle.btn_byh_stop.hide()
        self.byhanworkHandle.btn_byh_continue.show()

        if self.idx == 0:
            self.speed_module_pred = self.speed_module
            self.speed_module = {key: 0 for key in self.speed_module}  
            json_data = json.dumps(self.speed_module, ensure_ascii=False)
            self.pub_speed_module.publish(json_data)
        elif self.idx == 1:
            self.speed_dc_pred = self.speed_dc
            self.speed_dc = {key: 0 for key in self.speed_dc}  
            json_data = json.dumps(self.speed_dc, ensure_ascii=False)
            self.pub_speed_motor.publish(json_data)

    def continue_byhand(self):
        self.byhanworkHandle.btn_byh_stop.show()
        self.byhanworkHandle.btn_byh_continue.hide()

        if self.idx == 0:
            self.speed_module = self.speed_module_pred
            json_data = json.dumps(self.speed_module, ensure_ascii=False)
            self.pub_speed_module.publish(json_data)
        elif self.idx == 1:
            self.speed_dc = self.speed_dc_pred
            json_data = json.dumps(self.speed_dc, ensure_ascii=False)
            self.pub_speed_motor.publish(json_data)
    
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
        
        processed_image, check = self.process_image(cv_image)
        if check:
            labels = [
                self.autoworkHandle.lbl_inf_1,
                self.autoworkHandle.lbl_inf_2,
                self.autoworkHandle.lbl_inf_3,
                self.autoworkHandle.lbl_inf_4,
                self.autoworkHandle.lbl_inf_5
            ]
            
            for index, key in enumerate(self.data.keys()):
                if index < len(labels):
                    labels[index].setText(self.data[key])
                    labels[index].setWordWrap(True)
        # if self.data != self.prev_data:
        #     self.prev_data = self.data
        #     print("Day la: ", end="")
        #     print(self.prev_data)
        #     self.classify_product(self.data)
        
        qt_img = QImage(processed_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.autoworkHandle.lbl_img.setPixmap(pixmap.scaled(self.autoworkHandle.lbl_img.size(), Qt.KeepAspectRatio))

    def sub_callback_byh(self, image):
        cv_image = self.bridge.imgmsg_to_cv2(image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        
        h, w, ch = cv_image.shape
        # print(cv_image.shape)
        bytes_per_line = ch * w
        
        processed_image, check = self.process_image(cv_image)
        print(check)
        # if self.data:
        #     self.prev_data = self.data
        #     print("Day la: ", end="")
        #     print(self.data)
        #     self.classify_product(self.data)
        if check:
            labels = [
                self.byhanworkHandle.lbl_inf_1,
                self.byhanworkHandle.lbl_inf_2,
                self.byhanworkHandle.lbl_inf_3,
                self.byhanworkHandle.lbl_inf_4,
                self.byhanworkHandle.lbl_inf_5
            ]
            
            for index, key in enumerate(self.data.keys()):
                if index < len(labels):
                    labels[index].setText(self.data[key])
                    labels[index].setWordWrap(True)

        
        
        qt_img = QImage(processed_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        self.byhanworkHandle.lbl_img.setPixmap(pixmap.scaled(self.byhanworkHandle.lbl_img.size(), Qt.KeepAspectRatio))

    def update_image(self):
        # You may add functionality here if needed
        pass

    def process_image(self, frame):
        frame_flipped = cv2.flip(frame, 1)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(frame_flipped)
        check = False
        
        if data:
            print(type(data))
            self.data = json.loads(data)
        
        if self.compare_data():
            self.prev_data = self.data
            self.classify_product(data)
            check = True

        if bbox is not None:
            print("Waiting for QR code. Product Information:")
            print(self.data)

        return frame, check

    def compare_data(self):
      
        for key in self.data:
            if self.data[key] != self.prev_data[key]:
                return True
        return False

    def classify_product(self, qr_code_data ):
        my_db = MY_DB()
        my_db.connect("data.db")
        direction = ""
        if qr_code_data:
            print("Phân loại sản phẩm dựa trên thông tin từ mã QR code:", qr_code_data)
            # if qr_code_data['key'] == "xanh":
            #     direction = "1"
            # elif qr_code_data['key'] == "do":
            #     direction = "2"
            # elif qr_code_data['key'] == "vang":
            #     direction = "3"
            # self.pub_direction(direction)
            # check_value = my_db.check_value_exist(qr_code_data["key"])
            # if check_value:
            #     my_db.update_data("products", {"num": qr_code_data["num"]}, f"id = {qr_code_data['id']}")
            # else:
            #     my_db.insert_data("products",qr_code_data)
        else:
            print("Không tìm thấy mã QR code hoặc không thể đọc mã.")
    
    def dic_left(self):
        pub = rospy.Publisher("left_topic",String, queue_size=10)
        pub.publish("left")
    
    def dic_right(self):
        pub = rospy.Publisher("right_topic",String, queue_size=10)
        pub.publish("right")
    
    def dic_up(self):
        pub = rospy.Publisher("up_topic",String, queue_size=10)
        pub.publish("up")
    def dic_down(self):
        pub = rospy.Publisher("right_topic",String, queue_size=10)
        pub.publish("down")
    
    def imuCallback(self, imu_msg, choice):
        ax = imu_msg.linear_acceleration.x
        ay = imu_msg.linear_acceleration.y
        az = imu_msg.linear_acceleration.z
        
        angle = math.atan2(math.sqrt(ax**2+ay**2),az)*180.0/math.pi
        angle = "{:.2f}".format(angle)
        if choice == 1:
            self.autoworkHandle.lbl_axis.setText(angle)
        elif choice == 2:
            self.byhanworkHandle.lbl_axis.setText(angle)
        
    
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    
    app.exec_()