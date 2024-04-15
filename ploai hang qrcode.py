import cv2

def read_qr_code_from_camera():
  
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        detector = cv2.QRCodeDetector()    
        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            print("Đang đợi mã code. Thông tin sản phẩm:"+'\n', data)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return data
def classify_product(qr_code_data):
    if qr_code_data:
        print("Phân loại sản phẩm dựa trên thông tin từ mã QR code:", qr_code_data)
    else:
        print("Không tìm thấy mã QR code hoặc không thể đọc mã.")
if __name__ == "__main__":
    qr_code_data = read_qr_code_from_camera()
    classify_product(qr_code_data)
