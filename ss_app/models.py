from django.db import models

# Create your models here.

class Photos(models.Model):
    file_name = models.CharField(max_length=20)
    when_where = models.CharField(max_length=100)
    sort_order = models.IntegerField(default=0)
    caption = models.TextField()
    image = models.FileField(blank=True)
    
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='UploadedImage/')
    uploaded_at = models.DateTimeField(auto_now_add=True)