import os
import Image
import ImageOps

# load the index page template from file
curdir = os.path.abspath(".")
index_template_filename = curdir + "/index_template.html"
index_output_filename = curdir + "/static/index.html"

# read template for index.html into string
index_template_file = open(index_template_filename,'r')
index_template_string = index_template_file.read()
index_template_file.close()

def isJPG(string):
    return string.find(".JPG") != -1 and string.find(".thumbnail") == -1

folder_contents = os.listdir('./static/images')
images = filter(lambda(d):isJPG(d),folder_contents)

img_template = '<img data-slide="%d" class="thumbnail" src="%s" alt="">\n'
slide_template = '<div class="slide%d slide"><img alt=""></div>\n'
imgs_html = ""
slides_html = ""

# loop through images in folder, create and save thumbnail images, generate markup for thumbnail and lightbox "slide"
i = 1
# create thumbnail img tags and corresponding slides for each image in the images directory
for image in images:
    im = Image.open("./static/images/"+image)
    thumb = ImageOps.fit(im,(300,300),Image.ANTIALIAS)
    thumbnail_filename = "/images/thumbs/"+image.replace(".JPG","")+".thumbnail.JPG"
    thumb.save("./static"+thumbnail_filename)
    img_html = img_template % (i, thumbnail_filename)
    slide_html = slide_template % i
    imgs_html += img_html
    slides_html += slide_html
    i += 1

# place generated markup into index.html template string, write to index.html
compiled_index_template_string = index_template_string % (imgs_html, slides_html)
index_output_file = open(index_output_filename, 'w')
index_output_file.write(compiled_index_template_string)
index_output_file.close()
print "done"
