from django.core.exceptions import PermissionDenied
from django.contrib.contenttypes.models import ContentType


class AbstractBaseToggleService:
    repository_class = None       # Set in subclass
    feature_flag = None           # e.g., "allow_likes"

    def _check_allowed(self, obj):
        if not getattr(obj, self.feature_flag, False):
            raise PermissionDenied(f"{obj.__class__.__name__} does not support this action.")

    def toggle(self, user, obj):
        self._check_allowed(obj)
        return self.repository_class.toggle(user, obj)

    def get_status(self, user, obj):
        self._check_allowed(obj)
        return bool(self.repository_class.get_user_toggle(user, obj))

    def get_count(self, obj):
        return self.repository_class.model_class.objects.filter(
            content_type=ContentType.objects.get_for_model(obj.__class__),
            object_id=obj.id
        ).count()
