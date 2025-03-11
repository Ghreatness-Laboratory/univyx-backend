from rest_framework import serializers
from core.entertainment.models import articlesModel, comments
# from rest_framework import serializers
# from core.entertainment.services import *


class articlesModelSerializer(serializers.ModelSerializer):
    # Read-only fields (included in response but not accepted from users)
    author = serializers.StringRelatedField(read_only=True)  
    read_time = serializers.CharField(read_only=True)  
    excerpt = serializers.CharField(read_only=True)  

    class Meta:
        model = articlesModel
        fields = ['title', 'content', 'category', 'image', 'author', 'read_time', 'excerpt']  # Include all fields
        read_only_fields = ['author', 'read_time', 'excerpt']  # Prevent modification of these fields


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = comments
        fields = "__all__"
