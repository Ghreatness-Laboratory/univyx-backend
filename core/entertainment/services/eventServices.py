
from entertainment.serializers import eventsSerializer



### events/services/event_service.py

from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
# from events.repositories.event_repository import EventRepository
from shared.services import BaseService
# from shared.services.base_service import BaseService
from entertainment.repositories import EventRepository
from entertainment.models import Event


class EventService(BaseService):
    repository_class = EventRepository

    @staticmethod
    def validate_and_create_event(data):
        if data["end_time"] and data["start_time"] >= data["end_time"]:
            raise ValueError("End time must be after start time.")
        if data.get("is_recurring") and not data.get("recurrence_pattern"):
            raise ValueError("Recurring events need a recurrence pattern.")

        return EventService.create(**data)


















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