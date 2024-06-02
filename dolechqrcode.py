import cv2
import numpy as np

def angle_between_points(point, point1, point2):
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

def classify_product(qr_code_data):
    if qr_code_data:
        print("Phân loại sản phẩm dựa trên thông tin từ mã QR code:", qr_code_data)

def draw_dot_on_camera():
    cap = cv2.VideoCapture(2)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        center_x = 0
        center_y = 0

        if ret:
            # Đọc mã QR code từ camera và phân loại sản phẩm dựa trên mã QR code
            detector = cv2.QRCodeDetector()    
            data, bbox, _ = detector.detectAndDecode(frame)
            
            # Tọa độ của các điểm
            center_point = (356, 286)
            center_point1 = (180, 375)
            center_point1_2 = (521, 387)
            center_point1_3 = (366, 83)

            # Vẽ chấm trên frame
            cv2.circle(frame, center_point, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(frame, center_point1, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(frame, center_point1_2, radius=5, color=(0, 255, 0), thickness=-1)
            cv2.circle(frame, center_point1_3, radius=5, color=(0, 255, 0), thickness=-1)
            
            # Nối các điểm với nhau
            cv2.line(frame, center_point, center_point1, (0, 0, 255), 2)
            cv2.line(frame, center_point, center_point1_2, (0, 0, 255), 2)
            cv2.line(frame, center_point, center_point1_3, (0, 0, 255), 2)

            if data:
                classify_product(data)
                # Chuyển đổi bbox về định dạng numpy.ndarray
                bbox = bbox[0]
                bbox = bbox.astype(int)
                # Vẽ viền xung quanh mã QR code
                cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)
                
                # Tính tâm của mã QR code
                M = cv2.moments(bbox)
                if M["m00"] != 0:
                    center_x = int(M["m10"] / M["m00"])
                    center_y = int(M["m01"] / M["m00"])
                    # Vẽ tâm của mã QR code
                    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                    print("Tọa độ tâm:", center_x, center_y)
                    
                    # Tính góc lệch giữa center_point2 và đường thẳng được tạo bởi center_point và center_point1
                    angle = angle_between_points(center_point, center_point1, (center_x, center_y))
                    angle1 = angle_between_points(center_point, center_point1_2, (center_x, center_y))
                    angle2 = angle_between_points(center_point, center_point1_3, (center_x, center_y))

                    # Tìm góc nhỏ nhất
                    min_angle = min(angle1, angle2, angle)
                    cv2.putText(frame, "Min Angle: {:.2f}".format(min_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()

# Gọi hàm để vẽ chấm trên màn hình của camera
draw_dot_on_camera()
