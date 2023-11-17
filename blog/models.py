from django.db import models

# Create your models here.
class BlogModel(models.Model):
    name=models.CharField(default="",max_length=100)
    profile_img=models.CharField(default="",max_length=100)
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)