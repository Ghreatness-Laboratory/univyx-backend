from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone
import uuid
# from .BaseModel import BaseTimestampModel
from shared.models import BaseTimestampModel

class Event(BaseTimestampModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/events/')
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
        ordering = ['-date_created']
        verbose_name = "Event"
        verbose_name_plural = "Events"




