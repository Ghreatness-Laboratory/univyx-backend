from entertainment.models import News
from shared.repositories import BaseRepository

class NewsRepository(BaseRepository):
	model = News
    