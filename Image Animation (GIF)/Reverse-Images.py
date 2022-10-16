import os
from PIL import Image


images=[]
imagelist = os.listdir('apart') #lists images
imagelist.reverse() #reverses the order of the list

for i in imagelist:
    imgread = Image.open('apart/{}'.format(i))
    images.append(imgread)
images[0].save('reversed.gif', save_all=True, append_images = images[1:], duration=500, loop=0)