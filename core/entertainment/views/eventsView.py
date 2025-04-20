from rest_framework.viewsets import ModelViewSet
from shared.views.base_view import BaseContentAPIView
# from shared.mixins import CommentableMixin, BookmarkableMixin, LikableMixin
from entertainment.models import Article, News, Event
from entertainment.serializers import ArticleSerializer, NewsSerializer, EventSerializer
from entertainment.services import EventService

class EventAPIView(BaseContentAPIView):
    """
    View for managing Events. Supports creating, retrieving, and possibly other features like commenting, liking, etc.
    """
    serializer_class = EventSerializer
    service_class = EventService
    model_class = Event
