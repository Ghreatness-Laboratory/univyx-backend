from shared.Engagements.repository import LikeRepository
from shared.Engagements.services.basetoggleservice import AbstractBaseToggleService

class LikeService(AbstractBaseToggleService):
    repository_class = LikeRepository
    feature_flag = "allow_likes"
