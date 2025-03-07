from django.db import models

class eventsModel(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=250)
	description = models.TextField()
	image = models.ImageField(upload_to='uploads/eEvents')
	category = models.CharField(max_length=50)
	attendees = models.CharField(max_length=50)
	isRegistered = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title
	