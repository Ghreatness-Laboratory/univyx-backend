from rest_framework import serializers
from entertainment.models import Article
from shared.utils.file_uploads import Base64ImageField
from shared.models import Comment
from django.contrib.contenttypes.models import ContentType
from shared.Engagements.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    slug = serializers.ReadOnlyField()
    read_time = serializers.ReadOnlyField()
    excerpt = serializers.ReadOnlyField()
    date_created = serializers.ReadOnlyField()
    image = Base64ImageField(required=False, allow_null=True)

    is_bookmarked = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'slug', 'title', 'content', 'excerpt', 'read_time',
            'category', 'image', 'author', 'date_created',
            'is_bookmarked', 'is_liked', 'likes_count', 'comments'
        ]
        read_only_fields = [
        'id','slug','excerpt','read_time',
        'author','date_created','is_bookmarked',
        'likes_count','comments','is_liked'
        ]  # make all read-only unless specifically writing

    def get_is_bookmarked(self, obj):
        request = self.context.get('request')
        if obj.allow_bookmarks and request and request.user.is_authenticated:
            return obj.bookmarks.filter(user=request.user).exists()
        return False

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if obj.allow_likes and request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

    def get_likes_count(self, obj):
        return obj.likes.count() if obj.allow_likes else 0

    def get_comments(self, obj):
        if not obj.allow_comments:
            return []
        request = self.context.get('request')
        if request and request.query_params.get("include_comments") == "true":
            content_type = ContentType.objects.get_for_model(obj)
            comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk)
            return CommentSerializer(comments, many=True, context=self.context).data
        return []
