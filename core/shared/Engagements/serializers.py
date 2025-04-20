from rest_framework import serializers
from shared.models import Comment, Bookmark, Like

from rest_framework import serializers
from shared.models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # content = serializers.CharField(style={'base_template': 'textarea.html'}, max_length=1000)
    content = serializers.CharField()
    article = serializers.StringRelatedField(source='content_object', read_only=True)
    class Meta:
        model = Comment
        fields = ['article','id', 'user', 'content','created_at']
        read_only_fields = ['article','id','created_at','user']

    def get_target_object_title(self, obj):
        """Retrieve the title or name of the target object (e.g., article, event)."""
        target_object = obj.content_object  # Assuming content_object is a GenericForeignKey
        
        if hasattr(target_object, 'title'):  # For models like Article, News, etc.
            return target_object.title
        elif hasattr(target_object, 'name'):  # For models like Event
            return target_object.name

            
        return None  # Return None if no title or name attribute exists

    def validate_content(self, value):
        """Ensure the content is not empty or just whitespace."""
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        if len(value) < 5:  # Optional: Enforce a minimum length for the content
            raise serializers.ValidationError("Content is too short. Minimum length is 5 characters.")
        return value

    def create(self, validated_data):
        target_model = self.context.get('target_model')  # passed from view
        public_id = self.context.get('public_id')

        try:
            target_object = target_model.objects.get(public_id=public_id)
        except target_model.DoesNotExist:
            raise serializers.ValidationError("Target object not found")

        # Create the comment and associate it with the target object
        comment = Comment.objects.create(
            user=self.context['request'].user,
            content_object=target_object,
            content=validated_data.get('content', '')  # The validated content data
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

