from os import listdir
import Image
import ImageOps


def isJPG(string):
    return string.find(".JPG") != -1 and string.find(".thumbnail") == -1


folder_contents = listdir('.')
images = filter(lambda(d):isJPG(d),folder_contents)
for image in images:
    im = Image.open(image)
    thumb = ImageOps.fit(im,(300,300),Image.ANTIALIAS)
    thumb.save("thumbs/"+image.replace(".JPG","")+".thumbnail.JPG")

