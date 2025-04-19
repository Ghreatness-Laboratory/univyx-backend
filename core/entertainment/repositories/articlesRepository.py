from entertainment.models import Article
from shared.repositories import BaseRepository
# from .models import articlesModel
from django.db.models import Count
from django.utils.timezone import now
from django.db.models import QuerySet
from typing import Optional

class ArticleRepository(BaseRepository):
    model = Article
    
    @classmethod
    def create(cls, **kwargs):
        instance = cls.model(**kwargs)

        # If your model has these methods:
        # if hasattr(instance, 'generate_slug'):
        #     instance.slug = instance.generate_slug()

        if hasattr(instance, 'generate_excerpt'):
            instance.excerpt = instance.generate_excerpt()

        if hasattr(instance, 'generate_read_time'):
            instance.read_time = instance.generate_read_time()

        instance.save()
        return instance