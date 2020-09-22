import cv2


image = cv2.imread("hello.png")

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(image)

if bbox is not None:
    print(f"QRCode Data : {data}")
    

