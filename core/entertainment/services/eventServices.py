from core.entertainment.repositories import eventsRepository
from core.entertainment.serializers import eventsSerializer

class eventServices:
	@staticmethod
	def get_events():
		events = eventsRepository.getAllEvents()
		serialized = eventsSerializer(events, many=True)
		if serialized:
			return {"status":True,"data":serialized.data}
		return {"status":False, "error":"no events"}

	@staticmethod
	def get_event(id):
		event = eventsRepository.getEventById(id)
		serialized = eventsSerializer(event)
		if serialized:
			return {"status":True, "data":serialized.data}
		return {"status":False, "error":"event not found"}

	@staticmethod
	def create_new_event(request, data):
		event = eventsRepository.createEvent(*data.values())
		serialized = eventsSerializer(data=event)
		if serialized.is_valid:
			serialized.save()
			return {"status":True, "data":serialized.data}
		return {"status":True, "error":"error creating model"}