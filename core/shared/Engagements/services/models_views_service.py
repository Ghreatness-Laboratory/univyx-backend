# shared/engagements/services/view_service.py

from shared.engagements.repositories.view_repository import ViewRepository

class ViewService:
    repository_class = ViewRepository

    @classmethod
    def view(cls, user, obj):
        """
        Always create a new view event.
        """
        return cls.repository_class.create_view(user, obj)

    @classmethod
    def get_view_count(cls, obj):
        """
        Get total view count for an object.
        """
        return cls.repository_class.count_views(obj)
