from rest_framework.viewsets import ModelViewSet
from shared.views.base_view import BaseContentAPIView
# from shared.mixins import CommentableMixin, BookmarkableMixin, LikableMixin
from entertainment.models import Article, News, Event
from entertainment.serializers import ArticleSerializer, NewsSerializer, EventSerializer
from entertainment.services import NewsService
from shared.models import Comment,Like
from shared.Engagements.serializers import CommentSerializer,LikeSerializer

class NewsAPIView(BaseContentAPIView):
    """
    View for managing News content. Supports creating, retrieving, and liking.
    """
    serializer_class = NewsSerializer
    service_class = NewsService
    model_class = News
