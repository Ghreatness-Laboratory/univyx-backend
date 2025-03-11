from django.db import models 
from django.contrib.auth.models import User
import math

# user = get_user_model()

class articlesModel(models.Model):
	CATEGORY_CHOICES = [
        ('all','ALL'),
        ('student','student'),
        ('life','life'),
        ('campus life','Campus Life'),
        ('travel','Travel'),
        ('advice','Advice')
    ]
	title = models.CharField(max_length=200)
	excerpt = models.TextField(blank=True, null=True)
	content = models.TextField()
	author  = models.ForeignKey(User, on_delete=models.CASCADE)
	date  = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
	image  = models.ImageField(upload_to='uploads/article_img', null=True)
	# read_time = models.PositiveIntegerField()  # Stored in DB
	read_time = models.CharField(max_length=100, blank=True, editable=True)
	#num_of_likes  = models.PositiveIntegerField(default=0)
	#num_of_comments = models.PositiveIntegerField(default=0)
	# isBookmarked  
	# readtime  

	def calculate_read_time(self):
		"""
	    Recalculates and updates read time based on word count.
	    Did you know: The average human reads 200 words per min
	    time taken to read = 

		200 words per min 
		if read_time > 60m - read_time = in hours
	    """
		words_per_minute = 200  # Average reading speed
		total_words = len(self.content.split())

		read_time_minutes = total_words / words_per_minute
		read_time_seconds = math.ceil(read_time_minutes * 60)  # Convert to seconds

		if read_time_seconds < 60:
		    return f"{read_time_seconds} sec"
		else:
		    return f"{math.ceil(read_time_minutes)} min"
		# self.save(update_fields=["read_time"])


	def generate_excerpt(self):
		return self.content[:100] + "..." if len(self.content) > 100 else self.content


	@property
	def estimated_read_time(self):
		"""Returns stored read time but recalculates if missing."""
		if not self.read_time:
			# print('words')
			self.calculate_read_time()
		return self.calculate_read_time()

	def save(self, *args, **kwargs):
		"""Automatically updates read time when content changes."""
		print("pk ",self.pk)
		if self.pk:
		    old_instance = articlesModel.objects.filter(pk=self.pk).first()
		    # print(old_instance.content)
		    if old_instance and old_instance.content != self.content:
		        self.read_time = self.calculate_read_time();
		        self.excerpt = self.generate_excerpt();
		else:
			self.read_time = self.calculate_read_time();
			self.excerpt = self.generate_excerpt();
		# if not self.excerpt:
		# 	self.excerpt = self.content[:100] + "..." if len(self.content) > 100 else self.content
	    	# super().save(*arg, **kwargs)
		super().save(*args, **kwargs)

		

	@property
	def article_likesCount(self):
		return self.like_set.count()
	@property
	def article_commentsCounts(self):
		return self.comments.count()

	

class articleLikes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(articlesModel, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ("user","article")

	def __str__(self):
		return self.article

class comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(articlesModel, on_delete=models.CASCADE)
	text = models.TextField()
	# comment_like_count = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.article

	# @property
	# def comments_likesCount(self):
	# 	return self.like_set.count()


class commentLike(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.ForeignKey(comments, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ("user","comment")

	def __str__(self):
		return self.comment


		


		# student life
		# campus life
		# travel
		#  advice