from glob import glob
import Image

images = glob("static/images/*.JPG")
SHRINK_FACTOR = 1/2.0
# need to add a way of excluding images that are already acceptable sizes
# so, need to store dimensions that are deemed acceptable, and add a condition to the loop below

for image in images:
    im = Image.open(image)
    new_size = ( int(im.size[0]*SHRINK_FACTOR), int(im.size[1]*SHRINK_FACTOR) )
    im.thumbnail(new_size,Image.ANTIALIAS)
    im.save(image)
