from rest_framework.viewsets import ModelViewSet
from shared.views.base_view import BaseContentAPIView
# from shared.mixins import CommentableMixin, BookmarkableMixin, LikableMixin
from entertainment.models import Article, News, Event
from entertainment.serializers import ArticleSerializer, NewsSerializer, EventSerializer
from entertainment.services import ArticleService
from shared.models import Comment,Like,Bookmark
from shared.Engagements.serializers import CommentSerializer,BookmarkSerializer,LikeSerializer

class ArticleAPIView(BaseContentAPIView):
    """
    View for managing Articles. Supports creating, retrieving, commenting, liking, and bookmarking. 
    """
    serializer_class = ArticleSerializer
    service_class = ArticleService
    model_class = Article
