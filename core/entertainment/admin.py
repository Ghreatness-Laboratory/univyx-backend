from django.contrib import admin
from .models import articlesModel,NewsArticle,eventsModel
# Register your models here.

admin.site.register(articlesModel)
admin.site.register(NewsArticle)
admin.site.register(eventsModel)

