from rest_framework import serializers
from shared.models import Comment, Bookmark, Like, View

from rest_framework import serializers
from shared.models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    content = serializers.CharField()
    article = serializers.StringRelatedField(source='content_object', read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['article', 'id', 'user', 'content', 'created_at', 'likes']
        read_only_fields = ['article', 'id', 'created_at', 'user', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_target_object_title(self, obj):
        target_object = obj.content_object
        if hasattr(target_object, 'title'):
            return target_object.title
        elif hasattr(target_object, 'name'):
            return target_object.name
        return None

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        if len(value) < 5:
            raise serializers.ValidationError("Content is too short. Minimum length is 5 characters.")
        return value

    def create(self, validated_data):
        target_model = self.context.get('target_model')
        public_id = self.context.get('public_id')

        try:
            target_object = target_model.objects.get(public_id=public_id)
        except target_model.DoesNotExist:
            raise serializers.ValidationError("Target object not found")

        comment = Comment.objects.create(
            user=self.context['request'].user,
            content_object=target_object,
            content=validated_data.get('content', '')
        )
        return comment


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        target_model = self.context.get('target_model')  # passed from view
        public_id = self.context.get('public_id')

        try:
            target_object = target_model.objects.get(public_id=public_id)
        except target_model.DoesNotExist:
            raise serializers.ValidationError("Target object not found")

        # Create the comment and associate it with the target object
        bookmark = Bookmark.objects.create(
            user=self.context['request'].user,
            content_object=target_object,
        )
        return bookmark

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['id', 'user', 'created_at']

