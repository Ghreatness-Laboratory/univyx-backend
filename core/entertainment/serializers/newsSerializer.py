from core.entertainment.models import NewsArticle
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
	read_time = serializers.CharField(read_only=True)  
	description = serializers.CharField(read_only=True) 
	class Meta:
		model = NewsArticle
		fields = "__all__"
		# ['title','category','image','content','date','description','likes','read_time']
		read_only_fields = ['date','description','likes','read_time']