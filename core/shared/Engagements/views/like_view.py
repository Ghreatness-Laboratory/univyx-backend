from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shared.Engagements.utils import get_object_from_url
from shared.Engagements.services import LikeService

class LikeAPIView(APIView):
    service_class = LikeService

    def post(self, request, model_name, object_id):
        related_obj = get_object_from_url(model_name, object_id)
        result = self.service_class().toggle(request.user, related_obj)

        liked = isinstance(result, self.service_class.repository_class.model_class)
        count = self.service_class().get_count(related_obj)

        return Response({
            "liked": liked,
            "like_count": count
        }, status=status.HTTP_200_OK)

    def get(self, request, model_name, object_id):
        related_obj = get_object_from_url(model_name, object_id)
        liked = self.service_class().get_status(request.user, related_obj)
        count = self.service_class().get_count(related_obj)

        return Response({
            "liked": liked,
            "like_count": count
        }, status=status.HTTP_200_OK)
