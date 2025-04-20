from entertainment.repositories import ArticleRepository
from entertainment.models import articlesModel
from shared.services import BaseService
from entertainment.repositories import ArticleRepository



class ArticleService(BaseService):
    repository_class = ArticleRepository


