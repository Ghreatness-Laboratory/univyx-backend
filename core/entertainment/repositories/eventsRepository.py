from entertainment.models import Event
from shared.repositories import BaseRepository

class EventRepository(BaseRepository):
	model=Event 