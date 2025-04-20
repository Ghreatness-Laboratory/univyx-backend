# interactions/likes/repository.py

from django.contrib.contenttypes.models import ContentType
from shared.repositories.base_toggle_repository import BaseToggleRepository
from shared.models import Like

class LikeRepository(BaseToggleRepository):
    model_class = Like
