from core.entertainment.models import articlesModel

# from .models import articlesModel
from django.db.models import Count
from django.utils.timezone import now

class ArticleRepository:
	@staticmethod
	def getAllArticles():
		articles = articlesModel.objects.all()
		print(dir(articles))
		return articles

	@staticmethod
	def createArticle(title, content, category, image, user):
		"""Create a new article, setting all other fields internally."""
		article = articlesModel(
		    title=title,
		    content=content,
		    category=category,
		    image=image,
		    author=user,  # Automatically assign the logged-in user  # Set update time
		)
		article.excerpt = article.generate_excerpt()
		article.read_time = article.calculate_read_time()
		article.save()
		return article
	@staticmethod
	def update_article(article, content, category, image):
	    """Update an article while preventing users from modifying restricted fields."""
	    article.content = content
	    article.category = category
	    article.image = image
	    article.updated_at = now()  # Auto-update timestamp
	    article.excerpt = article.generate_excerpt()
	    article.read_time = article.calculate_read_time()
	    article.save()
	    return article





# def get_all_articles():
# 	return articlesModel.objects.all()

# def get_articles_by_id(article_id):
# 	return articlesModel.objects.filter(id=article_id).first()

# def create_article(**kwargs):
# 	# print(**kwargs)
# 	return articlesModel.objects.create(**kwargs)


# def update_article(article, **kwargs):
# 	for key, value in kwargs.items():
# 		""" 
# 			setattr(object, attribute_name, value)

# 			setattr(article, attribute_name, value)
# 			article is an instance of the article model

# 			so we get the particular instance we want to update 
# 			article = Article.objects.get(id=5) #for instance

# 			assume kwargs-kwargs holds a dict, is 
# 			kwargs = {
# 				'title': 'New Students Help',
# 				'content':'This is what new students need'
# 			}
# 			loop through kwargs
# 			for key, value in kwargs.item()
# 			first iteration:
# 			key = "title", value = "New Students Help"
# 			setattr(article, "title","New Students Help")
# 			second iteration
# 			key = "content", value = "This is what new students need"
# 			settattr(article, key, value)😊

# 		"""
# 		setattr(article, key, value)

# 	article.save() 
# 	return article 

# def delete_article(article):
# 	article.delete()