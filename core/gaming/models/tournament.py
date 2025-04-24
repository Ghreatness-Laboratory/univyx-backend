from django.db import models 

class tournaments(models.Model):
	image = models.ImageField(upload_to='tournaments/')
	name = models.CharField(max_length=300)
	description = models.TextField()
	category = models.CharField(max_length=50)
	link = models.CharField(max_length=500)