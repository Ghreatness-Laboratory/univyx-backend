from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shared.Engagements.utils import get_object_from_url
from shared.Engagements.services import BookmarkService

class BookmarkAPIView(APIView):
    """
        View for toggling bookmark...
    """
    service_class = BookmarkService

    def post(self, request, model_name, public_id):
        related_obj = get_object_from_url(model_name, public_id)
        result = self.service_class().toggle(request.user, related_obj)

        return Response({
            "bookmarked": isinstance(result, self.service_class.repository_class.model_class)
        }, status=status.HTTP_200_OK)

    def get(self, request, model_name, public_id):
        related_obj = get_object_from_url(model_name, public_id)
        bookmarked = self.service_class().get_status(request.user, related_obj)

        return Response({
            "bookmarked": bookmarked
        }, status=status.HTTP_200_OK)
