import cv2
import numpy

img = cv2.imread('imagepth')
qr_detect = cv2.QRCodeDetector() #define function

qr = qr_detect.detectAndDecode(img) #parameters: image path
data=qr[0]
bbox=qr[1].astype(numpy.int32).tolist()
bbox = bbox[0]

if bbox is not None:
    for i in range(len(bbox)):
        point1 = bbox[i]
        point2 = bbox[(i+1)%len(bbox)]
        cv2.line(img, point1, point2, color=(200,0,0), thickness = 20)


cv2.imshow('img',img)
cv2.waitkey(1000) #same function as time.sleep()
cv2.destroyAllWindows()
