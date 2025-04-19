from entertainment.models import News
from entertainment.repositories import NewsRepository
from entertainment.serializers import NewsSerializer

from shared.services import BaseService



class NewsService(BaseService):
    repository_class = NewsRepository

    @staticmethod
    def create_news(request, data):
        image = request.FILES.get("image")
        data = data.copy()
        data["image"] = image
        data["author"] = request.user

        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            news = NewsService.create(**serializer.validated_data)
            return {"status": True, "data": NewsSerializer(news).data}
        return {"status": False, "error": serializer.errors}






