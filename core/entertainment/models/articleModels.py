from django.db import models 
from django.contrib.auth.models import User

# user = get_user_model()

class articlesModel(models.Model):
	title = models.CharField(max_length=200)
	excerpt = models.TextField(blank=True, null=True)
	content = models.TextField()
	author  = models.ForeignKey(User, on_delete=models.CASCADE)
	date  = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=50)
	image  = models.ImageField(upload_to='uploads/article_img')
	#num_of_likes  = models.PositiveIntegerField(default=0)
	#num_of_comments = models.PositiveIntegerField(default=0)
	# isBookmarked  
	# readtime  

	def save(self, *arg, **kwargs):
		if not self.excerpt:
			self.excerpt = self.content[:100] + "..." if len(self.content) > 100 else self.content
			super().save(self,*arg, **kwargs)

	@property
	def likesCount(self):
		return self.like_set.count()
	@property
	def commentsCounts(self):
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
	comment_like_count = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.article

class CommentLike(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.ForeignKey(comments, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ("user","comment")

	def __str__(self):
		return self.comment


		