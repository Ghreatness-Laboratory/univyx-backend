from core.entertainment.repositories import eventsRepository
from core.entertainment.serializers import eventsSerializer



### events/services/event_service.py

from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
# from events.repositories.event_repository import EventRepository
from events.models import Event

class EventService:

    @staticmethod
    def validate_event_data(data):
        start = data.get('start_time')
        end = data.get('end_time')
        is_recurring = data.get('is_recurring', False)
        recurrence = data.get('recurrence_pattern')

        if start and end and end <= start:
            raise ValidationError("End time must be after start time.")
        if is_recurring and not recurrence:
            raise ValidationError("Recurring events must have a recurrence pattern.")
        if not is_recurring:
            data['recurrence_pattern'] = None
        return data

    @staticmethod
    def create_event(data):
        data = EventService.validate_event_data(data)
        if not data.get('slug'):
            data['slug'] = slugify(data['title'])
        return EventRepository.create(**data)

    @staticmethod
    def update_event(event: Event, data):
        data = EventService.validate_event_data(data)
        if 'title' in data:
            data['slug'] = slugify(data['title'])
        return EventRepository.update(event, **data)

    @staticmethod
    def delete_event(event: Event):
        return EventRepository.delete(event)

    @staticmethod
    def get_event_by_id(event_id: int):
        return EventRepository.get_by_id(event_id)

    @staticmethod
    def get_event_by_slug(slug: str):
        return EventRepository.get_by_slug(slug)

    @staticmethod
    def list_events():
        return EventRepository.all()




















# class eventServices:
# 	@staticmethod
# 	def get_events():
# 		events = eventsRepository.getAllEvents()
# 		serialized = eventsSerializer(events, many=True)
# 		if serialized:
# 			return {"status":True,"data":serialized.data}
# 		return {"status":False, "error":"no events"}

# 	@staticmethod
# 	def get_event(id):
# 		event = eventsRepository.getEventById(id)
# 		serialized = eventsSerializer(event)
# 		if serialized:
# 			return {"status":True, "data":serialized.data}
# 		return {"status":False, "error":"event not found"}

# 	@staticmethod
# 	def create_new_event(request, data):
# 		event = eventsRepository.createEvent(*data.values())
# 		serialized = eventsSerializer(data=event)
# 		if serialized.is_valid:
# 			serialized.save()
# 			return {"status":True, "data":serialized.data}
# 		return {"status":True, "error":"error creating model"}