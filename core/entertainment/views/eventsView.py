from rest_framework.views import APIView
from rest_framework.response import Response
from core.entertainment.services import eventServices

class eventsView(APIView):
	def get(self,request):
		events =eventServices.get_events()
		return Response(events)