import cv2
import numpy

img = cv2.imread('imagepth')
qr_detect = cv2.QRCodeDetector() #define function

qr = qr_detect.detectAndDecode(img) #parameters: image path
print(qr[0])