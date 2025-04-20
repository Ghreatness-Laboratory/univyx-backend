from shared.repositories.base_repository import BaseRepository
from shared.models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentRepository(BaseRepository):
    model_class = Comment

    @classmethod
    def get_all(cls, related_obj):
        return cls.model_class.objects.filter(
            content_type=ContentType.objects.get_for_model(related_obj.__class__),
            object_id=related_obj.id
        )

    @classmethod
    def create(cls, data):
        return cls.model_class.objects.create(**data)
