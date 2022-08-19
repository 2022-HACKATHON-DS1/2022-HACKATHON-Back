from email.mime import image
from django.db import models

class Text(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class Image(models.Model):
    image = models.ImageField(blank=True, upload_to='my_image')

    def get_image(self):
        return self.image