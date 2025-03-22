from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
	path('articles/',articlesAPIView.as_view()),
	path('news/', NewsView.as_view()),
	path('events/', eventsView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)