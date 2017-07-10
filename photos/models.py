from django.db import models
from PIL import Image


class Photo(models.Model):
    MAX_WIDTH = 1300
    MAX_HEIGHT = 1300
    THUMBNAIL_SIZE = (300, 300)

    image = models.ImageField(upload_to="gallery_photos", null=False, blank=False,
                              height_field="height", width_field="width")
    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s (%dx%d)- %s" % (self.title or "Untitled", self.width, self.height, self.date)

    def fit_image(self):
        print("fitting image...")
        self.image.open()
        original_image = Image.open(self.image)
        dimension_to_max_ratios = [original_image.size[0] / float(Photo.MAX_WIDTH),
                                   original_image.size[1] / float(Photo.MAX_HEIGHT)]
        largest_ratio = max(dimension_to_max_ratios)
        if largest_ratio > 1:
            new_size = (int(original_image.size[0] / largest_ratio), int(original_image.size[1] / largest_ratio))
            print("%s was too big at %s,\nnew_size: %s" % (self.image.path, str(original_image.size), str(new_size)))
            original_image.thumbnail(new_size, Image.ANTIALIAS)
            original_image.save(self.image.path, format="JPEG", quality=100)
            self.width = new_size[0]
            self.height = new_size[1]
        else:
            print("dimensions were okay")

    def save(self, *args, **kwargs):
        print("in save method of Photo")
        super(Photo, self).save(*args, **kwargs)
        print("after super save of Photo")
        self.fit_image()
        super(Photo, self).save(*args, **kwargs)
