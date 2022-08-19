from django.contrib import admin
from .models import Post
from frameapp import models as models

# Register your models here.
admin.site.register(Post)
admin.site.register(models.Text)