from glob import glob
import Image

images = glob("*.JPG")
SHRINK_FACTOR = 1/2.0

for image in images:
    im = Image.open(image)
    new_size = ( int(im.size[0]*SHRINK_FACTOR), int(im.size[1]*SHRINK_FACTOR) )
    im.thumbnail(new_size,Image.ANTIALIAS)
    im.save(image)
