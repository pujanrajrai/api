from django.db import models

# Create your models here.


class PictureDesc(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='picture')