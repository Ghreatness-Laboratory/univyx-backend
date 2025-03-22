from core.entertainment.models import NewsArticle

class NewsRepository:
	@staticmethod
	def getAllNews():
		news = NewsArticle.objects.all()
		return news

	@staticmethod
	def getNewsById(news_id):
		news_single = NewsArticle.objects.get(id=news_id)
		return news_single

	def create_new_news(title, category, content, image, user):
		new_news = NewsArticle(
			title= title,
			category=category,
			content = content,
			image=image,
			user=user
			)
		new_news.description = NewsArticle.generate_detail()
		new_news.read_time = NewsArticle.calculate_read_time()
		new_news.save()
		return new_news 