from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

import uuid
import math

User = get_user_model()

# ------------------ ABSTRACT BASE MODELS ------------------ #
from django.utils.text import slugify

class BaseTimestampModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public_id = models.IntegerField(unique=True, db_index=True, null=True, blank=True,editable=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug and hasattr(self, 'title') and self.title:
            self.slug = slugify(self.title)

        if not self.public_id:
            # Assign the next available integer
            last = self.__class__.objects.aggregate(models.Max("public_id"))["public_id__max"] or 0
            self.public_id = last + 1
        super().save(*args, **kwargs)


class ReadableContentModel(models.Model):
    content = models.TextField()
    read_time = models.CharField(max_length=50, blank=True, editable=False)
    excerpt = models.TextField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True

    def calculate_read_time(self):
        words_per_minute = 200
        total_words = len(self.content.split()) if self.content else 0
        read_time_minutes = total_words / words_per_minute
        read_time_seconds = math.ceil(read_time_minutes * 60)

        return f"{read_time_seconds} sec" if read_time_seconds < 60 else f"{math.ceil(read_time_minutes)} min"

    def generate_excerpt(self):
        if self.content:
            clean_content = self.content.strip()
            return clean_content[:100] + "..." if len(clean_content) > 100 else clean_content
        return ""

    def save(self, *args, **kwargs):
        if self.pk:
            old = type(self).objects.filter(pk=self.pk).only('content').first()
            if old and old.content == self.content:
                return super().save(*args, **kwargs)
        self.read_time = self.calculate_read_time()
        self.excerpt = self.generate_excerpt()
        super().save(*args, **kwargs)




class Event(BaseTimestampModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to=f'uploads/events/{self.__class__}')
    is_recurring = models.BooleanField(default=False)
    recurrence_pattern = models.CharField(
        max_length=20,
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
            ('yearly', 'Yearly')
        ],
        blank=True,
        null=True
    )

    def clean(self):
        if self.start_time and self.end_time and self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        if self.is_recurring and not self.recurrence_pattern:
            raise ValidationError("Please select a recurrence pattern for recurring events.")
        if not self.is_recurring:
            self.recurrence_pattern = None

    def __str__(self):
        return self.title

    @property
    def time_range(self):
        if self.start_time and self.end_time:
            return f"{self.start_time.strftime('%I:%M%p').lower()} - {self.end_time.strftime('%I:%M%p').lower()}"
        elif self.start_time:
            return self.start_time.strftime('%I:%M%p').lower()
        return ""

    class Meta:
        abstract=True
        ordering = ['-date_created']





class ContentBaseModel(BaseTimestampModel, ReadableContentModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True)
    category = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class ImgAbs(models.Model):
    upload_to= None
    image = models.ImageField(upload_to=upload_to, null=True)

    class Meta:
        abstract = True


# ------------------ GENERIC RELATIONAL MODELS ------------------ #

class AbstractContentTypeCBLV(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_user',
        editable=False,
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_content_type'
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        unique_together = ('user', 'content_type', 'object_id')



class Bookmark(AbstractContentTypeCBLV):
    def __str__(self):
        return f"{self.user} bookmarked {self.content_object}"

class Like(AbstractContentTypeCBLV):
    def __str__(self):
        return f"{self.user} liked {self.content_object}"

class Comment(AbstractContentTypeCBLV):
    allow_likes = True
    content = models.TextField()
    likes = GenericRelation(Like)
    def __str__(self):
        return f"{self.user} on {self.content_object}"

class View(AbstractContentTypeCBLV):
    def __str__(self):
        return f"{self.user} viewed {self.content_object}"

