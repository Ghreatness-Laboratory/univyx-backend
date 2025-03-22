from core.entertainment.models import Event
from django.db import models
from django.utils import timezone
from django.db.models import QuerySet
from typing import Optional

class EventRepository:

    @staticmethod
    def all() -> QuerySet:
        return Event.objects.all()

    @staticmethod
    def get_by_id(event_id: int) -> Optional[Event]:
        return Event.objects.filter(id=event_id).first()

    @staticmethod
    def get_by_slug(slug: str) -> Optional[Event]:
        return Event.objects.filter(slug=slug).first()

    @staticmethod
    def create(**kwargs) -> Event:
        return Event.objects.create(**kwargs)

    @staticmethod
    def update(event: Event, **kwargs) -> Event:
        for attr, value in kwargs.items():
            setattr(event, attr, value)
        event.save()
        return event

    @staticmethod
    def delete(event: Event):
        event.delete()
















# class eventsRepository:
# 	@staticmethod
# 	def getAllEvents():
# 		events = eventsModel.objects.all()
# 		return events

# 	@staticmethod
# 	def getEventById(id):
# 		event = eventsModel.objects.get(id=id)
# 		return event

# 	@staticmethod
# 	def createEvent(title,date,time,location,description,image):
# 		event = eventsModel(
# 			title=title,
# 			date=date,
# 			time=time,
# 			description=description,
# 			image=image
# 		)
# 		event.save()
# 		return event
