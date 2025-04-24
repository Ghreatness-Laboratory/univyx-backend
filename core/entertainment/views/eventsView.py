from rest_framework.viewsets import ModelViewSet
from shared.views.base_view import BaseContentAPIView
# from shared.mixins import CommentableMixin, BookmarkableMixin, LikableMixin
from entertainment.models import Article, News, entertainmentEventModel
from entertainment.serializers import ArticleSerializer, NewsSerializer, entertainmentEventSerializer
from entertainment.services import entertainmentEventService

class EventAPIView(BaseContentAPIView):
    """
    View for managing Events. Supports creating, retrieving, and possibly other features like commenting, liking, etc.
    """
    serializer_class = entertainmentEventSerializer
    service_class = entertainmentEventService
    model_class = entertainmentEventModel
