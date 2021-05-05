from django.db import models

# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='nralif/blog/photo')
    short_description =  models.TextField()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)