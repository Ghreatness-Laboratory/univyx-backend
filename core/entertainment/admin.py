from django.contrib.contenttypes.admin import GenericTabularInline
from shared.models import Comment
from django.contrib import admin
from .models import Article,News,entertainmentEventModel
# Register your models here.



@admin.register(entertainmentEventModel)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_range', 'location', 'is_recurring', 'recurrence_pattern')
    list_filter = ('date', 'is_recurring', 'recurrence_pattern')
    search_fields = ('title', 'location', 'description')
    

class CommentInline(GenericTabularInline):
    model = Comment
    ct_field = "content_type"   # Tells Django what field holds the content type
    ct_fk_field = "object_id"   # Tells Django what field holds the object ID
    extra = 1  # Number of extra comment forms to show


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

    list_display = ('title', 'author','category','total_likes','total_comments','total_views')  # Optional, customize as needed
    list_filter = ('category',)
# admin.site.register(Article, ArticleAdmin)
admin.site.register(News)


