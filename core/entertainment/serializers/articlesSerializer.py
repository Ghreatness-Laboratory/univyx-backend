from rest_framework import serializers
from ..models import articlesModel, comments



class articlesModelSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    class Meta:
        model = articlesModel
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = comments
        fields = "__all__"
