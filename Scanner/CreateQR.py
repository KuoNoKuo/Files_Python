from PIL import Image
import qrcode 

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CONNECT_H, box_size=8, border=4)

# Parameters:

qr.add_data('Welcome to MonkeyBalls!')
qr.make(fit=True)

img=qr.make_image()
img=img.convert('RGBA')
logo=Image.open('FILERIRECTORY')
img_w, img_h =  img.size
factor=4
size_w = int(img_w/factor)
size_h = int(img_h/factor)
logo_w, logo_h = logo.size

if logo_w > size_w or logo_h > size_h:
    logo_w = size_w
    logo_h = size_h

logo = logo.resize((logo_w,logo_h), Image.ANTIALIAS).convert('RGBA')
#center the image 
pos_x = int((img_w-logo_w)/2)
pos_y = int((img_h-logo_h)/2)

img.paste(logo, (pos_x,pos_y))
img.show()
img.save('example.png') #save the image