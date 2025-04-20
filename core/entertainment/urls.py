from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from .views import ArticleAPIView, NewsAPIView, EventAPIView
from shared.Engagements.views import CommentAPIView,LikeAPIView,BookmarkAPIView
# from entertainment.views.comment_views import CommentAPIView
article_view = ArticleAPIView.as_view()

news_view = NewsAPIView.as_view()

event_view = EventAPIView.as_view()


# from interactions.comments.views import CommentAPIView

urlpatterns = [
    # 🔹 Articles
    path("articles/", ArticleAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleAPIView.as_view(), name="article-detail"),
    path("news/", news_view, name="article-list"),
    path("events/", event_view, name="article-list"),

    path('<str:model_name>/<int:public_id>/comments/', CommentAPIView.as_view()),
    # 🔹 Comments for an article
    path('<str:model_name>/<int:object_id>/like/', LikeAPIView.as_view()),
    path('<str:model_name>/<int:public_id>/bookmark/', BookmarkAPIView.as_view()),

]
# urls.py



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)