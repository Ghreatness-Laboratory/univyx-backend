from core.entertainment.models import eventsModel

class eventsRepository:
	@staticmethod
	def getAllEvents():
		events = eventsModel.objects.all()
		return events

	@staticmethod
	def getEventById(id):
		event = eventsModel.objects.get(id=id)
		return event

	@staticmethod
	def createEvent(title,date,time,location,description,image):
		event = eventsModel(
			title=title,
			date=date,
			time=time,
			description=description,
			image=image
		)
		event.save()
		return event
