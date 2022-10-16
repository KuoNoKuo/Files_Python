import os #Operating System to grant access to documents 
#pillow
from PIL import Image

gif = Image.open('what.gif')
os.mkdir('apart')


try: #tries
    i = 0
    while True:
        gif.seek(i)
        gif.save('results/{}.png'.format(i))
        i+=1
except: #it will try until something wrong happens
    pass