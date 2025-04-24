from rest_framework import serializers
from django.utils.text import slugify



class EventSerializer(serializers.ModelSerializer):
    
    model_service = None
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    time_range = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()
    date_created = serializers.ReadOnlyField()
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        abstract=True
        model = None
        fields = [
            'id', 'title', 'slug', 'date',
            'start_time', 'end_time', 'time_range', 'location', 'description',
            'image', 'is_recurring', 'recurrence_pattern',
            'date_created'
        ]
        read_only_fields= ['date_created','id']

    def validate(self, data):
        return model_service.validate_event_data(data.copy())

    def create(self, validated_data):
        return model_service.create_event(validated_data)

    def update(self, instance, validated_data):
        return model_service.update_event(instance, validated_data)

    def get_fields(self):
        fields = super().get_fields()
        user = self.context['request'].user if self.context.get('request') else None
        if user and not user.is_staff:
            fields['is_recurring'].read_only = True
            fields['recurrence_pattern'].read_only = True
        return fields



