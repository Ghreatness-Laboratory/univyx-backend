from django.db import models
from shared.models import Event

class gamingEventsModel(Event):
	class Meta:
		verbose_name = "Gaming_Event"
		verbose_name_plural = "Gaming_Events"
