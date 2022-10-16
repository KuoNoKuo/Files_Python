import os #Operating System to grant access to documents 
#pillow
from PIL import Image

gif = Image.open('Image Animation (GIF)/what.gif')
os.mkdir('apart')


try: #tries
    i = 0
    while True:
        gif.seek(i)
        gif.save('apart/{}.png'.format(str(i).rjust(3,'0'))) #after the format - It will make the file name 3 digits, if not 3 digits it will replace the unit with 0
        i+=1
except: #it will try until something wrong happens
    pass