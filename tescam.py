<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Long Sentence Example')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Create a QLabel
        label = QLabel()
        
        # Set the long sentence as text
        long_sentence = "This is a very long sentence that needs to be displayed in a QLabel without being cut off. PyQt5 allows us to adjust properties such as word wrap to ensure the entire sentence is visible."
        label.setText(long_sentence)

        # Set word wrap to true
        label.setWordWrap(True)

        # Add the label to the layout
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
=======
#!/usr/bin/python3
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def publish_image():
    """Capture frames from a camera and publish it to the topic /image_raw
    """
    image_pub = rospy.Publisher("image_raw", Image, queue_size=10)
    bridge = CvBridge()
    capture = cv2.VideoCapture("/dev/video0")

    while not rospy.is_shutdown():
        # Capture a frame
        ret, img = capture.read()
        if not ret:
            rospy.ERROR("Could not grab a frame!")
            break
        # Publish the image to the topic image_raw
        try:
            img_msg = bridge.cv2_to_imgmsg(img, "bgr8")
            image_pub.publish(img_msg)
        except CvBridgeError as error:
            print(error)

if __name__=="__main__":
    rospy.init_node("my_cam", anonymous=True)
    print("Image is being published to the topic /image_raw ...")
    publish_image()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
>>>>>>> 2542a42e6b3bdd52084d22447e81cea35590f49f
