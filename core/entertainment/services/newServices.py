from core.entertainment.models import NewsArticle
from core.entertainment.repositories import NewsRepository
from core.entertainment.serializers import NewsSerializer

class NewsService:
	@staticmethod
	def get_all_news_service():
		news= NewsRepository.get_all_news()
		serialized = NewsSerializer(news, many=True)
		return serialized.data 

	@staticmethod
	def get_single_news_service(news_id):
		news_single = NewsRepository.objects.get(id=news_id)
		if news_single:
			return {'status':True, 'data': NewsSerializer(news_single).data}

		return {'status':False, 'error':'Article not found'}

	@staticmethod
	def create_new_news_service(request, data):
		image = request.FILES.get("image")  # Retrieve the uploaded file
		data = data.copy()
		data["image"] = image  # Attach the image file to data

		serialized = NewsSerializer(data=data)
		if serialized.is_valid():
			news = NewsRepository.create_new_news(
					title=data["title"],
					content=data["content"],
					category=data["category"],
					image=image,
					user=request.user
				)
			return {"status":True,"data":NewsSerializer(news).data}
		return {"status":False,"error": serialized.errors}











