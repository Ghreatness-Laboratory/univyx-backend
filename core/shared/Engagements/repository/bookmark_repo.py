from django.contrib.contenttypes.models import ContentType
from shared.repositories.base_toggle_repository import BaseToggleRepository
from shared.models import Bookmark

class BookmarkRepository(BaseToggleRepository):
    model_class = Bookmark
