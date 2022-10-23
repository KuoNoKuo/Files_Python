#Add text to a gif (every frame)
import os 
from PIL import Image, ImageDraw, ImageFont #import Library names are quite self explanatory 

images=[]

imagelist = os.listdir('Image Animation (GIF)/apart')
imagelist.reverse()

fontpath = '' #font path
font = ImageFont.truetype(fontpath, 30) #parameters are font and font size.

for _ in imagelist:
    imgread = Image.open('Image Animation (GIF)/apart/{}'.format(_))
    draw= ImageDraw.Draw(imgread)
    r,g,b= 30,30,30
    draw.text((50,50),'text here', font=font, fill=(r,g,b))
    images.append(imgread)
images[0].save('newgif.gif', save_all=True, append_images=images[1:0])

os.system("newgif.gif") #open a file  or document 