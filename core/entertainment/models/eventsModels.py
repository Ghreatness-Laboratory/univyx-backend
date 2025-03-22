from django.db import models

class eventsModel(models.Model):
	title = models.CharField(max_length=200)
	# date = models.DateTimeField()#user should input a date
	date = models.DateField(null=True,blank=True)
	time = models.CharField(max_length=10,null=True,blank=True)
	# time = models.TimeField(null=True,blank=True)
	location = models.CharField(max_length=250)
	description = models.TextField()
	image = models.ImageField(upload_to='uploads/eEvents')
	date_created = models.DateTimeField(auto_now_add=True,editable=False,null=True)
	# category = models.CharField(max_length=50)


	def __str__(self):
		print(self.time.split("-"))
		return self.title

	def save(self, *args,**kwargs):
		valid_time_am = [f"{x}am" for x in range(1,13)]
		valid_time_pm = [f"{x}pm" for x in range(1,13)]
		valid_time= valid_time_am + valid_time_pm
		print(valid_time)
		for vals in self.time.split('-'):
			if vals not in valid_time or vals not in valid_time:
				raise ValueError('not a valid date')
		super().save(*args, **kwargs)

	 