from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from core.entertainment.models import *
from core.entertainment.serializers import *
# from core.entertainment.forms import myForm
from core.entertainment.services import *



class articlesAPIView(APIView):
    # parser_classes = [FormParser, MultiPartParser]
    # renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):
        print(request.data)
        # articles = articlesModel.objects.all()
        # articleSerializer = articlesModelSerializer(articles, many=True)
        data = ArticleService.get_articles()
        # form = myForm()
        return Response(data)

    def post(self, request):
        print('request: ',request.data)
        
        result = ArticleService.create_article(request, request.data)
        if result["status"]:
            print(result)
            return Response(result["data"], status=status.HTTP_201_CREATED)
        return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        
class CommentAPIView(APIView):

    def get(self, request, post_id):
        """Retrieve all comments for an article"""
        article = get_object_or_404(articlesModel, id=post_id)
        comments = article.comments.all().order_by("-created_at")  # Latest comments first
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        """Add a new comment to an article"""
        article = get_object_or_404(articlesModel, id=post_id)
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




