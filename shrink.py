from glob import glob
import Image

# need to add a way of excluding images that are already acceptable sizes
# so, need to store dimensions that are deemed acceptable, and add a condition to the loop below
MAX_WIDTH = 1900
MAX_HEIGHT = 1900

def shrink_images():
    images = glob("static/images/*.JPG")
    for image in images:
        im = Image.open(image)
        dimension_to_max_ratios = [ im.size[0]/float(MAX_WIDTH), im.size[1]/float(MAX_HEIGHT) ]
        largest_ratio = max(dimension_to_max_ratios)
        if largest_ratio > 1:
            new_size = ( int(im.size[0]/largest_ratio), int(im.size[1]/largest_ratio) )
            print "%s was too big at %s,\nnew_size: %s" % (image, str(im.size), str(new_size))
            im.thumbnail(new_size,Image.ANTIALIAS)
            im.save(image)
        else: 
            print "%s is fine at %s" % (image, str(im.size))
        print "--------------------------------------"


if __name__ == "__main__":
    shrink_images()
