from rest_framework import serializers
from core.entertainment.models import eventsModel

class eventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = eventsModel
		fields= '__all__'
		read_only_fields = ['date_created']