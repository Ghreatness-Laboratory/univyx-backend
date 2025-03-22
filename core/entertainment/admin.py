from django.contrib import admin
from .models import articlesModel,NewsArticle,Event
# Register your models here.



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_range', 'location', 'is_recurring', 'recurrence_pattern')
    list_filter = ('date', 'is_recurring', 'recurrence_pattern', 'timezone')
    search_fields = ('title', 'location', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(articlesModel)
admin.site.register(NewsArticle)


