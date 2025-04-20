# interactions/comments/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shared.Engagements.serializers import CommentSerializer
from shared.Engagements.services import CommentService
from shared.Engagements.utils import get_object_from_url

from django.shortcuts import get_object_or_404

class CommentAPIView(APIView):
    """
        View for creating comments:
            {
                content: "whatever"
            }
            and hit post
    """
    service_class = CommentService

    def get(self, request, model_name, public_id):
        related_obj = get_object_from_url(model_name, public_id)
        comments = self.service_class().get(related_obj)
        serializer = CommentSerializer(comments, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, model_name, public_id):
        target_obj = get_object_from_url(model_name, public_id)
        serializer = CommentSerializer(data=request.data, context={
            'request': request,
            'target_model': target_obj.__class__,
            'public_id': public_id,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

