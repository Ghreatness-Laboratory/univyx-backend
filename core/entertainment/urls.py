from django.urls import path
from .views import *

urlpatterns = [
	path('',articlesAPIView.as_view()),
]