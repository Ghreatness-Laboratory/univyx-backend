# shared/engagements/views/view_api.py (updated)

from shared.base_view import BaseContentAPIView
from shared.engagements.services.view_service import ViewService

from rest_framework.response import Response
from rest_framework import status

class ViewAPIView(BaseContentAPIView):
    service_class = ViewService

    def post(self, request, *args, **kwargs):
        user = request.user
        obj = self.get_target_object()

        self.service_class.view(user, obj)
        view_count = self.service_class.get_view_count(obj)

        return Response({
            "detail": "View recorded successfully.",
            "total_views": view_count
        }, status=status.HTTP_201_CREATED)

    def get_target_object(self):
        model_name = self.kwargs.get('model_name')
        public_id = self.kwargs.get('public_id')

        if not model_name or not public_id:
            raise NotFound('Model name and public_id must be provided in the URL.')

        try:
            model = apps.get_model('core', model_name.capitalize())
        except LookupError:
            raise NotFound(f"Model '{model_name}' not found.")

        obj = model.objects.filter(public_id=public_id).first()
        if not obj:
            raise NotFound(f"{model_name.capitalize()} with ID {public_id} not found.")

        return obj
