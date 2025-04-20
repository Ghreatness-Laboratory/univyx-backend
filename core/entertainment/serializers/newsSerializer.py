from entertainment.models import News
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
	# author = serializers.HiddenField(default=serializers.CurrentUserDefault())

	read_time = serializers.CharField(read_only=True)  
	description = serializers.CharField(read_only=True) 
	like_count = serializers.SerializerMethodField()
	class Meta:
		model = News
		fields = ['title','category','image','content','description','like_count','read_time']
		read_only_fields = ['date','description','likes','read_time']


	def get_like_count(self, obj):
	    return obj.likes.count()
