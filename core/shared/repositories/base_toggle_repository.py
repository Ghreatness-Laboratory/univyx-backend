# repositories/base_toggle_repository.py
from django.contrib.contenttypes.models import ContentType
from shared.repositories.base_repository import BaseRepository

class BaseToggleRepository(BaseRepository):
    model_class = None  # Set in subclasses

    @classmethod
    def get_user_toggle(cls, user, obj):
        return cls.model_class.objects.filter(
            user=user,
            content_type=ContentType.objects.get_for_model(obj.__class__),
            object_id=obj.id
        ).first()

    @classmethod
    def is_toggled(cls, user, obj):
        return cls.get_user_toggle(user, obj) is not None

    @classmethod
    def toggle(cls, user, obj):
        existing = cls.get_user_toggle(user, obj)
        if existing:
            existing.delete()
            return False
        return cls.model_class.objects.create(
            user=user,
            content_type=ContentType.objects.get_for_model(obj.__class__),
            object_id=obj.id
        )
