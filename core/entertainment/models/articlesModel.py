from django.db import models
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from shared.models import ContentBaseModel, Comment, Bookmark, Like, View, BaseTimestampModel
User = get_user_model()


class ArticleManager(models.Manager):
    def get_trending(self):
        time_window = now() - timedelta(hours=5)

        return self.annotate(
            likes_count=Count('likes', filter=Q(likes__created_at__gte=time_window)),
            comments_count=Count('comments', filter=Q(comments__created_at__gte=time_window)),
            views_count=Count('views', filter=Q(views__created_at__gte=time_window)),
        ).annotate(
            trending_score=ExpressionWrapper(
                F('likes_count') * 1 +
                F('comments_count') * 2 +
                F('views_count') * 0.5,
                output_field=FloatField()
            )
        ).order_by('-trending_score')


class Article(ContentBaseModel):
    allow_comments = True
    allow_bookmarks = True
    allow_likes = True

    CATEGORY_CHOICES = [
        ('all', 'All'),
        ('student', 'Student'),
        ('life', 'Life'),
        ('campus', 'Campus Life'),
        ('travel', 'Travel'),
        ('advice', 'Advice'),
    ]

    objects = ArticleManager()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all')

    # ✅ Correct field names
    comments = GenericRelation(Comment)
    likes = GenericRelation(Like)
    bookmarks = GenericRelation(Bookmark)
    views = GenericRelation(View)


    class Meta:
        app_label = 'entertainment'
        ordering = ['-date_created']

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return self.comments.count()

    @property
    def total_views(self):
        return self.views.count()

    def is_bookmarked_by(self, user):
        return self.bookmarks.filter(user=user).exists()

    def __str__(self):
        return self.title


class HotTopics(BaseTimestampModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/HotTopics/', null=True)
    category = models.CharField(max_length=50)
    allow_comments = True
    discussions = GenericRelation(Comment)

    class Meta:
        app_label = 'entertainment'
        ordering = ['-date_created']


    @property
    def total_discussions(self):
        return self.discussions.count()

