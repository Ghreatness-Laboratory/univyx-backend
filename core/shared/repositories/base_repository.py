# BaseRepository class
from django.db import models
from django.db.models import QuerySet
from typing import Optional

class BaseRepository:

    model: models.Model = None  # To be defined in subclasses

    @classmethod
    def get_all(cls) -> QuerySet:
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, object_id) -> Optional[models.Model]:
        return cls.model.objects.filter(public_id=object_id).first()

    @classmethod
    def create(cls, **kwargs) -> models.Model:
        instance = cls.model(**kwargs)
        instance.save()
        return instance

    @classmethod
    def update(cls, instance: models.Model, **kwargs) -> models.Model:
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, instance: models.Model):
        instance.delete()
