import qrcode
import cv2
import json

qr_code = """
    {"id":1}
"""

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_code)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save("choma.png")

def decode_qr_code(image_path):
    image = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    if data:
        data = json.loads(data)
        print("QR Code Data:", data)
    else:
        print("No QR code found in the image")

image_path = "choma.png"

decode_qr_code(image_path)
