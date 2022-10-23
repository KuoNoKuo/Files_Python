import cv2

bc_detect = cv2.barcode_BarcodeDetector()

img = cv2.imread('Image_Path')

is_ok, bar_info, bar_type, pos = bc_detect.detectAndDecode(img)

print(
    is_ok, bar_info, bar_type, pos
)
