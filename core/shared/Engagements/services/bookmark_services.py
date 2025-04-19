from shared.Engagements.repository import BookmarkRepository
from shared.Engagements.services.basetoggleservice import AbstractBaseToggleService

class BookmarkService(AbstractBaseToggleService):
    repository_class = BookmarkRepository
    feature_flag = "allow_bookmarks"
