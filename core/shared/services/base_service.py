from typing import Type

class BaseService:
    repository_class: Type = None  # Must be set by child classes

    @classmethod
    def list(cls):
        return cls.repository_class.get_all()

    @classmethod
    def retrieve(cls, pk):
        """Retrieve an object by its primary key."""
        instance = cls.repository_class.get_by_id(pk)
        if not instance:
            raise ValueError("Object not found")
        return instance

    @classmethod
    def create(cls, validated_data):
        return cls.repository_class.create(**validated_data)

    @classmethod
    def update(cls, instance, validated_data):
        return cls.repository_class.update(instance, **validated_data)

    @classmethod
    def delete(cls, instance):
        return cls.repository_class.delete(instance)
