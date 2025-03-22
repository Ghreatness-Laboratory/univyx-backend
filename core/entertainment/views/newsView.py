from core.entertainment.services import NewsService
from rest_framework.views import APIView
from rest_framework.response import Response

class NewsView(APIView):
	def get(self, request):
		new_news = NewsService.get_all_news_service()
		return Response(new_news)

	def post(self, request):
        # print('request: ',request.data)
        
		result = NewsService.create_new_news_service(request, request.data)
		if result["status"]:
		    print(result)
		    return Response(result["data"], status=status.HTTP_201_CREATED)
		return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
