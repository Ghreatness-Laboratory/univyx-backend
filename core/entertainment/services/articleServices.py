from core.entertainment.repositories import ArticleRepository
from core.entertainment.models import articlesModel
from core.entertainment.serializers import articlesModelSerializer




class ArticleService:
	@staticmethod
	def get_articles():
		article = ArticleRepository.get_articles()
		serialized = articlesModelSerializer(article, many=True)
		return serialized.data
		

	@staticmethod
	def get_article(article_id):
	    """Retrieve an article and return serialized data."""
	    article = ArticleRepository.get_article_by_id(article_id)
	    if article:
	        return {"status": True, "data": articlesModelSerializer(article).data}
	    return {"status": False, "error": "Article not found"}

	@staticmethod
	def create_article(request, data):
	    """Create an article, handle file upload, and return the response."""
	    image = request.FILES.get("image")  # Retrieve the uploaded file
	    data = data.copy()
	    data["image"] = image  # Attach the image file to data

	    serializer = articlesModelSerializer(data=data)
	    if serializer.is_valid():
	        article = ArticleRepository.create_article(
	            title=data["title"],
	            content=data["content"],
	            category=data["category"],
	            image=image,  # Pass uploaded file
	            user=request.user
	        )
	        print(article.read_time)
	        return {"status": True, "data": articlesModelSerializer(article).data}
	    
	    return {"status": False, "error": serializer.errors}

	


	@staticmethod
	def update_article(article, content, category, image):
	    """Updates an article while preventing users from modifying restricted fields."""
	    return ArticleRepository.update_article(article, content, category, image)

        
