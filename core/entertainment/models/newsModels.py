from django.db import models
from shared.models import ContentBaseModel
from shared.models import Comment,Bookmark,Like
import math
from django.contrib.contenttypes.fields import GenericRelation

class News(ContentBaseModel):
    allow_comments = False
    allow_bookmarks= False
    allow_likes = True

    CATEGORY_CHOICES = [
        ('all', 'All'),
        ('environment', 'Environment'),
        ('campus', 'Campus'),
        ('sports', 'Sports'),
        ('academics', 'Academics'),
        ('research', 'Research')
    ]
    image = models.ImageField(upload_to='uploads/news/', null=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all')

    # likes = models.PositiveIntegerField(default=0, editable=False)
    likes = GenericRelation(Like)
    # bookmarks = GenericRelation(Bookmark)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
        verbose_name = "News"
        verbose_name_plural = "News"
