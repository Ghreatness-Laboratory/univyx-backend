from django.db import models

# Create your models here.

class Store(models.Model):
	image = models.ImageField(upload_to='/store/')
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	tags = models.CharField(max_length=200)
	link = models.CharField(max_length=500)

