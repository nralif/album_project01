from django.db import models

# Create your models here.
class album(models.Model):


    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='nralif/album/photo/')