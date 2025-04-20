# shared/engagements/repositories/view_repository.py

from shared.models import View
from shared.repositories.base_repository import BaseRepository
from django.contrib.contenttypes.models import ContentType

class ViewRepository(BaseRepository):
    model = View

    @classmethod
    def create_view(cls, user, obj):
        """
        Always create a new view record.
        """
        return cls.model.objects.create(
            user=user,
            content_type=ContentType.objects.get_for_model(obj.__class__),
            object_id=obj.id
        )

    @classmethod
    def count_views(cls, obj):
        """
        Count how many times this object has been viewed.
        """
        return cls.model.objects.filter(
            content_type=ContentType.objects.get_for_model(obj.__class__),
            object_id=obj.id
        ).count()
