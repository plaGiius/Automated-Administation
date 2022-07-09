import cv2
# read the QRCODE image
img = cv2.imread("/users/girishkrithik/desktop/cv.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:Successfull\n{data}")
else:
    print("sus:Invalid Certificate")

