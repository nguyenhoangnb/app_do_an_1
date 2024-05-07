from handle import autoHandle
from handle import programHandle
from handle import autoworkHandle
from handle import manualHandle
from pysql import *
from APP import auto_start

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

direction = {"green":"001",
            "red":"100",
            "blue":"010",
}

speed_module = {
    "Module 1":0,
    "Module 2":0,
    "Module 3":0,
    "Module 4":0
}


pre_data = {
    "id":1,
    "color":"redd",
    "address":"a",
    "type":"a",
    "price":0.1
}

data = {
    "id":0,
    "color":"red",
    "address":"",
    "type":"",
    "price":0.0
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
        self.speed = ""
        self.speed0 = ""
        self.data = data
        self.prev_data = pre_data
        self.direction = direction
        self.speed_module = speed_module
        self.speed_module_pred = speed_module
        #program UI
        self.programUi = QMainWindow()
        self.programHandle = programHandle(self.programUi)
        self.programHandle.btn_pro_auto.clicked.connect(lambda:self.automation())
        self.programHandle.btn_pro_manual.clicked.connect(lambda:self.manual())
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
        #manual UI
        self.manualUI = QMainWindow()
        self.manualHandle = manualHandle(self.manualUI)
        self.manualHandle.btn_manual_back.clicked.connect(lambda:self.back_to_main())
        self.manualHandle.btn_manual_set.clicked.connect(lambda: self.set_speed_manual(self.idx))
        self.manualHandle.btn_manual_start.clicked.connect(lambda: self.start_manual())
        self.manualHandle.btn_manual_stop.clicked.connect(lambda: self.stop_manual())
        self.manualHandle.btn_manual_continue.clicked.connect(lambda: self.continue_manual())
        self.manualHandle.btn_manual_module_1.clicked.connect(lambda: self.dic_module_1())
        self.manualHandle.btn_manual_module_2.clicked.connect(lambda: self.dic_module_2())
        self.manualHandle.btn_manual_module_3.clicked.connect(lambda: self.dic_module_3())
        
        #Topic name
        self.topic_img = "image_raw"
        self.topic_speed_auto = "speed_auto"
        self.topic_speed_by_module = "speed_module"
        self.topic_speed_by_motor = "speed_motor"
        self.topic_speed = "control_signal"
        self.topic_imu = "handsfree/imu"
        self.bridge = CvBridge()
        self.programUi.show()
        self.timer = QTimer()
        self.mode = 1
        self.capture = cv2.VideoCapture(0)
        # self.start = False
        # self.timer.timeout.connect(lambda:self.insert_table_auto())
        # self.timer.timeout.connect(lambda:self.insert_table_manual())
        # self.timer.start(10)
        self.check = False
        rospy.init_node("img_node", anonymous=True)
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
            self.topic_speed,
            String,
            queue_size=10
        )
     
       
    def automation(self):
        self.programUi.hide()
        self.autoUI.show()
        self.programUi.close()
        self.autoworkUI.close()
        self.manualUI.close()
        
        
    def startauto(self):
        self.autoUI.hide()
        self.autoUI.close()
        self.programUi.close()
        self.manualUI.close()
        self.autoworkUI.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_auto())
        # self.timer.start(100)  
        
        # self.show_img_automation()
        
        self.sub_imu = rospy.Subscriber(
            self.topic_imu,
            Imu,
            lambda msg: self.imuCallback(msg,1)
        )
        self.pub_out_timer = QTimer()
        self.timer.timeout.connect(self.show_img_automation)
        self.timer.start(1000//30) 
        
    
       
    def back_to_main(self):
        self.autoUI.hide()
        self.autoworkUI.hide()
        self.manualUI.hide()
        self.programUi.show()
        self.autoUI.close()
        self.autoworkUI.close()
        self.manualUI.close()    
    #set speed auto
    def set_speed_auto(self):
        text = self.autoHandle.cb_auto_speed.currentText()
        self.pub_speed_auto = rospy.Publisher(
            self.topic_speed_auto,
            Int16,
            queue_size=10
        )
        # rate = rospy.Rate(1)
        if text == "High speed":
            self.mode = 1
        if text == "Normal speed":
            self.mode = 2
        if text == "Slow speed":
            self.mode = 3
        
    def stop_auto(self):
        self.speed_dc_pred = self.speed_dc
        self.autoworkHandle.btn_auw_stop.hide()
        self.autoworkHandle.btn_auw_continue.show()
        for x in self.speed_dc:
            self.speed_dc[x] = 0
        self.speed0 = f"M0{direction}0|0|0|M2{direction}0|0|0|"
        self.pub_direction.publish(self.speed0)
        
    def continue_auto(self):
        self.speed_dc = self.speed_dc_pred
        self.autoworkHandle.btn_auw_stop.show()
        self.autoworkHandle.btn_auw_continue.hide()
        self.pub_direction.publish(self.speed)
    def back_auto_work(self):
        self.autoworkUI.hide()
        self.autoUI.show()
        self.autoworkUI.close()
        
    def manual(self):
        self.programUi.hide()
        self.manualUI.show()
        self.programUi.close()
        self.autoUI.close()
        self.autoworkUI.close()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.insert_table_manual())
        self.manualHandle.btn_manual_continue.hide()
        self.sub_imu = rospy.Subscriber(
            self.topic_imu,
            Imu,
            lambda msg: self.imuCallback(msg,2)
        )
        # rospy.Timer(rospy.Duration(1), self.update_image)
        self.manualHandle.cbox_manual_function.currentIndexChanged.connect(self.manual_change)
        self.timer.timeout.connect(self.sub_callback_manual)
        self.timer.start(1000//30)  
       
        self.manualHandle.btn_manual_set.clicked.connect(lambda: self.set_speed_manual(self.idx))
    
    def manual_change(self, idx):
        print(idx)
        if idx == 0:
            self.manualHandle.cb_manual_module.show()
            self.manualHandle.cb_manual_motor.hide()
        elif idx == 1:
            self.manualHandle.cb_manual_module.hide()
            self.manualHandle.cb_manual_motor.show()
        self.idx = idx
        
    def set_speed_manual(self, current_idx):
        if current_idx == 1:
            dc = self.manualHandle.plt_manual_speed.toPlainText()
            idx = self.manualHandle.cb_manual_motor.currentText()
            if (not self.kiem_tra(dc)):
                print(dc)
                self.manualHandle.plt_manual_speed.setPlainText("0")
            else:
                self.speed_dc[idx] = int(self.manualHandle.plt_manual_speed.toPlainText())
                
            print(self.speed_dc)
        elif current_idx == 0:
            mod_speed = self.manualHandle.plt_manual_speed.toPlainText()
            idx_mod = self.manualHandle.cb_manual_module.currentText()
            print(idx_mod)
            if not self.kiem_tra(mod_speed):
                self.manualHandle.plt_manual_speed.setPlainText("0")
            else:
                self.speed_module[idx_mod] = int(self.manualHandle.plt_manual_speed.toPlainText())
            print(mod_speed)
            
    def start_manual(self):
        self.manualHandle.btn_manual_continue.hide()
        self.manualHandle.btn_manual_stop.show()
        if self.idx == 0:
            json_data = json.dumps(self.speed_module, ensure_ascii=False)
            speed = f"M0"
            self.pub_speed_module.publish(json_data)
        elif self.idx == 1:
            json_data = json.dumps(self.speed_dc, ensure_ascii=False)
            self.pub_speed_motor.publish(json_data)
            
    def stop_manual(self):
        self.manualHandle.btn_manual_stop.hide()
        self.manualHandle.btn_manual_continue.show()
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

    def continue_manual(self):
        self.manualHandle.btn_manual_stop.show()
        self.manualHandle.btn_manual_continue.hide()

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
        self.autoworkHandle.tbl_auto_quantity.setRowCount(0)
        self.result = mydb.select_all("consumer_goods")
        label = ["id", "color", "amount"]
        label1 = mydb.get_table_columns("consumer_goods") 
        self.autoworkHandle.tbl_auto_quantity.setColumnCount(len(label))
        self.autoworkHandle.tbl_auto_quantity.setHorizontalHeaderLabels(label)
        for row_num, row_data in enumerate(self.result):
            self.autoworkHandle.tbl_auto_quantity.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                if label1[col_num] == "color" or label1[col_num] == "id" or label1[col_num] == "amount":
                    self.autoworkHandle.tbl_auto_quantity.setItem(row_num, col_num, QTableWidgetItem(str(col_data))) 
        mydb.close()
    def insert_table_manual(self):
        mydb = MY_DB()
        mydb.connect("data.db")
        self.manualHandle.tbl_manual_quantity.setRowCount(0)
        self.result = mydb.select_all("consumer_goods")
        label = ["id", "color", "amount"]
        label1 = mydb.get_table_columns("consumer_goods")  
        self.manualHandle.tbl_manual_quantity.setColumnCount(len(label))
        self.manualHandle.tbl_manual_quantity.setHorizontalHeaderLabels(label)
        for row_num, row_data in enumerate(self.result):
            self.manualHandle.tbl_manual_quantity.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                if label1[col_num] == "color" or label1[col_num] == "id" or label1[col_num] == "amount":
                    self.manualHandle.tbl_manual_quantity.setItem(row_num, col_num, QTableWidgetItem(str(col_data))) 
        mydb.close()
        
    def kiem_tra(self,xau):
        return bool(re.match(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', xau))
    
    def angle_between_points(self,point, point1, point2):
        # Tính vector từ point đến point1 và từ point đến point2
        vector1 = np.array([point1[0] - point[0], point1[1] - point[1]])
        vector2 = np.array([point2[0] - point[0], point2[1] - point[1]])

        # Tính độ dài của các vector
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)

        # Tính góc lệch bằng arccos của dot product giữa hai vector
        dot_product = np.dot(vector1, vector2)
        angle_radians = np.arccos(dot_product / (norm1 * norm2))

        # Chuyển đổi từ radian sang độ
        angle_degrees = np.degrees(angle_radians)
        return angle_degrees
    
    def show_img_automation(self):
        ret, cv_image = self.capture.read()
        if ret:
            center_point = (int(cv_image.shape[1] / 2), int(cv_image.shape[0] / 2))
            center_point1 = (80, 385)
            center_point1_2 = (540, 385)
            center_point1_3 = (313, 50)

            # Vẽ chấm trên cv_image
            cv2.circle(cv_image, center_point, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(cv_image, center_point1, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(cv_image, center_point1_2, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(cv_image, center_point1_3, radius=5, color=(0, 255, 0), thickness=-1)
            
            # Nối các điểm với nhau
            cv2.line(cv_image, center_point, center_point1, (0, 0, 255), 2)
            cv2.line(cv_image, center_point, center_point1_2, (0, 0, 255), 2)
            cv2.line(cv_image, center_point, center_point1_3, (0, 0, 255), 2)

            if data:
                # classify_product(data)
                # Chuyển đổi bbox về định dạng numpy.ndarray
                bbox = bbox[0]
                bbox = bbox.astype(int)
                # Vẽ viền xung quanh mã QR code
                cv2.polylines(cv_image, [bbox], True, (0, 255, 0), 2)
                
                # Tính tâm của mã QR code
                M = cv2.moments(bbox)
                if M["m00"] != 0:
                    center_x = int(M["m10"] / M["m00"])
                    center_y = int(M["m01"] / M["m00"])
                    # Vẽ tâm của mã QR code
                    cv2.circle(cv_image, (center_x, center_y), 5, (0, 0, 255), -1)
                    print("Tọa độ tâm:", center_x, center_y)
                    
                    # Tính góc lệch giữa center_point2 và đường thẳng được tạo bởi center_point và center_point1
                    angle = self.angle_between_points(center_point, center_point1, (center_x, center_y))
                    angle1 = self.angle_between_points(center_point, center_point1_2, (center_x, center_y))
                    angle2 = self.angle_between_points(center_point, center_point1_3, (center_x, center_y))

                    # Tìm góc nhỏ nhất
                    min_angle = min(angle1, angle2, angle)
                    cv2.putText(cv_image, "Min Angle: {:.2f}".format(min_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            h, w, ch = cv_image.shape
            bytes_per_line = ch * w
            self.check = self.process_image(cv_image)
            qt_img = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_img)
            self.autoworkHandle.lbl_img.setPixmap(pixmap.scaled(self.autoworkHandle.lbl_img.size(), Qt.KeepAspectRatio))
            if self.check:
                self.classify_product(self.data)
                mydb = MY_DB()
                mydb.connect("data.db")
                if not mydb.check_value_exist("consumer_goods","id",self.data["id"]) and self.data["id"]!=0:
                    mydb.insert_data("consumer_goods",{"id":self.data["id"]} )
                if mydb.check_value_exist("consumer_goods", "id",self.data["id"]):
                    mydb.update_amount("consumer_goods",{"id":self.data["id"]})
                mydb.close()
                labels_name = [
                    self.autoworkHandle.lbl_auw_3,
                    self.autoworkHandle.lbl_auw_4,
                    self.autoworkHandle.lbl_auw_5,
                    self.autoworkHandle.lbl_auw_6,
                    self.autoworkHandle.lbl_auw_7
                ]
                labels_inf = [
                    self.autoworkHandle.lbl_inf_1,
                    self.autoworkHandle.lbl_inf_2,
                    self.autoworkHandle.lbl_inf_3,
                    self.autoworkHandle.lbl_inf_4,
                    self.autoworkHandle.lbl_inf_5
                ]
                
                for index, key in enumerate(self.data.keys()):
                    if index < len(labels_inf):
                        labels_name[index].setText(key)
                        labels_inf[index].setText(str(self.data[key]))
                        labels_inf[index].setWordWrap(True)
                self.check = False
 
    def sub_callback_manual(self):
        # cv_image = self.bridge.imgmsg_to_cv2(image)
        # capture = cv2.VideoCapture("/dev/video0")
        ret, cv_image = self.capture.read()
        if ret:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            h, w, ch = cv_image.shape
            bytes_per_line = ch * w
            
            self.check = self.process_image(cv_image)
            qt_img = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_img)
            self.manualHandle.lbl_img.setPixmap(pixmap.scaled(self.manualHandle.lbl_img.size(), Qt.KeepAspectRatio))
            
            if self.check:
                self.classify_product(self.data)
                mydb = MY_DB()
                mydb.connect("data.db")
                if not mydb.check_value_exist("consumer_goods","id",self.data["id"]) and self.data["id"]!=0:
                    mydb.insert_data("consumer_goods",{"id":self.data["id"]} )
                if mydb.check_value_exist("consumer_goods", "id",self.data["id"]):
                    mydb.update_amount("consumer_goods",{"id":self.data["id"]})
                mydb.close()
                labels_name = [
                    self.manualHandle.lbl_manual_2,
                    self.manualHandle.lbl_manual_3,
                    self.manualHandle.lbl_manual_4,
                    self.manualHandle.lbl_manual_5,
                    self.manualHandle.lbl_manual_6
                ]
                labels_inf = [
                    self.manualHandle.lbl_manual_inf_1,
                    self.manualHandle.lbl_manual_inf_2,
                    self.manualHandle.lbl_manual_inf_3,
                    self.manualHandle.lbl_manual_inf_4,
                    self.manualHandle.lbl_manual_inf_5
                ]
                
                for index, key in enumerate(self.data.keys()):
                    if index < len(labels_inf):
                        labels_name[index].setText(key)
                        labels_inf[index].setText(str(self.data[key]))
                        labels_inf[index].setWordWrap(True)
                self.check = False
            
    def process_image(self, frame):
        frame_flipped = cv2.flip(frame, 1)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(frame_flipped)
        check = False
        if data:
            self.data = json.loads(data)
        if data and self.compare_data() :
            self.prev_data = self.data
            check = True

        if bbox is not None:
            # print("Waiting for QR code. Product Information:")
            pass

        return check

    def compare_data(self):
      
        for key in self.data:
            if self.data[key] != self.prev_data[key]:
                return True
        return False

    def classify_product(self, qr_code_data :dict):
        module = 0
        color = qr_code_data.get("color")
        if qr_code_data:
            print("Classify product base on qrcode:", qr_code_data)
            if color == "green":
                module = 1
            elif color == "red":
                module = 2
            elif color == "blue":
                module = 3
            print(direction)    
            if self.mode == 1:
                self.speed = f"M0{self.direction[color]}255|255|0|M{module}{self.direction[color]}255|255|0|"
                self.speed0 = f"M0{self.direction[color]}0|0|0|M{module}{self.direction[color]}0|0|0|"
            elif self.mode == 2:
                self.speed = f"M0{self.direction[color]}255|0|255|M{module}{self.direction[color]}255|0|255|"
                self.speed0 = f"M0{self.direction[color]}|0|0|M{module}{self.direction[color]}0|0|0|"
                pass
            elif self.mode == 3:
                self.speed = f"M0{self.direction[color]}|255|255|M{module}{self.direction[color]}0|255|255|"
                self.speed0 = f"M0{self.direction[color]}0|0|0|M{module}{self.direction[color]}0|0|0|"
                pass
            self.pub_direction.publish(self.speed)
            
            QTimer.singleShot(5000, lambda:self.set_speed_to_zero(self.speed0))

        else:
            print("No Qrcode found or unable to read Qrcode")
    def set_speed_to_zero(self, speed0):
        self.pub_direction.publish(speed0)
    def dic_module_1(self):
        pub = rospy.Publisher("module_1_topic",String, queue_size=10)
        pub.publish("module_1")
    
    def dic_module_2(self):
        pub = rospy.Publisher("module_2_topic",String, queue_size=10)
        pub.publish("module_2")
    
    def dic_module_3(self):
        pub = rospy.Publisher("module_3_topic",String, queue_size=10)
        pub.publish("module_3")
   
    
    def imuCallback(self, imu_msg, choice):
        ax = imu_msg.linear_acceleration.x
        ay = imu_msg.linear_acceleration.y
        az = imu_msg.linear_acceleration.z
        
        angle = math.atan2(math.sqrt(ax**2+ay**2),az)*180.0/math.pi
        angle = "{:.2f}".format(angle)
        ax = "{:.2f}".format(ax)
        ay = "{:.2f}".format(ay)
        if choice == 1:
            self.autoworkHandle.lbl_axis.setText(angle)
            self.autoworkHandle.lbl_auw_X_value.setText(str(ax))
            self.autoworkHandle.lbl_auw_Y_value.setText(str(ay))
        elif choice == 2:
            self.manualHandle.lbl_axis.setText(angle)
            self.manualHandle.lbl_manual_x_value.setText(str(ax))
            self.manualHandle.lbl_manual_y_value.setText(str(ay))
    
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    
    app.exec_()