from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BaseContentAPIView(APIView):
    """
    Abstract base view to support CRUD operations for models (like articles).
    Handles core DRF APIView responsibilities and delegates extended behavior to subclasses.
    """

    model_class = None          # Set in subclass (e.g., Article)
    serializer_class = None     # Set in subclass (e.g., ArticleSerializer)
    service_class = None        # Set in subclass (e.g., ArticleService)

    def get_object(self, pk):
        return self.service_class.retrieve(pk)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print('news')
        if pk:
            instance = self.get_object(pk)
            print('inside news')
            if not instance:
                return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

            return Response(self.serializer_class(instance).data)
        else:
            queryset = self.service_class.list()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = self.service_class.create(serializer.validated_data)
            return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = self.get_object(pk)
        if not instance:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            instance = self.service_class.update(instance, serializer.validated_data)
            return Response(self.serializer_class(instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = self.get_object(pk)
        if not instance:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        self.service_class.delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

