from os import listdir
import Image
import ImageOps


def isJPG(string):
    return string.find(".JPG") != -1 and string.find(".thumbnail") == -1


folder_contents = listdir('.')
images = filter(lambda(d):isJPG(d),folder_contents)
img_template = '<img data-slide="%d" class="thumbnail" src="static/images/%s" alt="">\n'
slide_template = '<div class="slide%d slide"><img alt=""></div>\n'
imgs_html = ""
slides_html = ""
i = 1
for image in images:
    im = Image.open(image)
    thumb = ImageOps.fit(im,(300,300),Image.ANTIALIAS)
    thumbnail_filename = "thumbs/"+image.replace(".JPG","")+".thumbnail.JPG"
    thumb.save(thumbnail_filename)
    img_html = img_template % (i, thumbnail_filename)
    slide_html = slide_template % i
    imgs_html += img_html
    slides_html += slide_html
    i += 1

print imgs_html
print slides_html
