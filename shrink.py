# this file shrinks the images in the images folder. (to half the original size, by default)
# this was just a quick n dirty solution to the fact that the images I was working with were larger than I wanted to host
from glob import glob
import Image

images = glob("static/images/*.JPG")
SHRINK_FACTOR = 1/2.0

for image in images:
    im = Image.open(image)
    new_size = ( int(im.size[0]*SHRINK_FACTOR), int(im.size[1]*SHRINK_FACTOR) )
    im.thumbnail(new_size,Image.ANTIALIAS)
    im.save(image)
