from shared.services.base_service import BaseService
from django.core.exceptions import PermissionDenied
from django.contrib.contenttypes.models import ContentType
from shared.Engagements.repository import CommentRepository


class CommentService(BaseService):
    repository_class = CommentRepository
    feature_flag = "allow_comments"

    def _check_allowed(self, obj):
        if not getattr(obj, self.feature_flag, False):
            raise PermissionDenied(f"{obj.__class__.__name__} does not support comments.")

    def create(self, related_obj, user, data):
        self._check_allowed(related_obj)

        content_type = ContentType.objects.get_for_model(related_obj.__class__)
        data.update({
            'content_type': content_type,
            'object_id': related_obj.id,
            'user': user
        })
        return self.repository_class.create(data)

    def get(self, related_obj):
        self._check_allowed(related_obj)
        return self.repository_class.get_all(related_obj)
