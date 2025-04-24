from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone
import uuid
# from .BaseModel import BaseTimestampModel
from shared.models import BaseTimestampModel,Event

class entertainmentEventModel(Event):
    class Meta:
        verbose_name = "Entertainment_Event"
        verbose_name_plural = "Entertainment_Events"




