from rest_framework import serializers
from entertainment.models import entertainmentEventModel
from shared.serializers import EventSerializer
from entertainment.services import entertainmentEventService
from django.utils.text import slugify


#make this an abstract class
class entertainmentEventSerializer(EventSerializer):
    model_service = entertainmentEventService
    class Meta:
        model = entertainmentEventModel







# from rest_framework import serializers
# from core.entertainment.models import Event
# from django.utils.text import slugify
# from django.core.exceptions import ValidationError
# from datetime import datetime


# class EventSerializer(serializers.ModelSerializer):
#     time_range = serializers.ReadOnlyField()
#     slug = serializers.ReadOnlyField()
#     date_created = serializers.ReadOnlyField()

#     class Meta:
#         model = Event
#         fields = [
#             'id',
#             'title',
#             'slug',
#             'date',
#             'start_time',
#             'end_time',
#             'time_range',
#             'timezone',
#             'location',
#             'description',
#             'image',
#             'is_recurring',
#             'recurrence_pattern',
#             'date_created',
#         ]

#     def validate(self, data):
#         start = data.get('start_time')
#         end = data.get('end_time')
#         is_recurring = data.get('is_recurring')
#         recurrence_pattern = data.get('recurrence_pattern')

#         # Validate time range
#         if start and end and end <= start:
#             raise serializers.ValidationError("End time must be after start time.")

#         # Validate recurrence
#         if is_recurring and not recurrence_pattern:
#             raise serializers.ValidationError("Please select a recurrence pattern if the event is recurring.")
#         if not is_recurring:
#             data['recurrence_pattern'] = None  # Clean up data

#         return data

#     def create(self, validated_data):
#         # Automatically create a slug if it's not present
#         if not validated_data.get('slug'):
#             validated_data['slug'] = slugify(validated_data['title'])

#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         # Ensure slug is updated only if title changes
#         if 'title' in validated_data:
#             instance.slug = slugify(validated_data['title'])

#         return super().update(instance, validated_data)
