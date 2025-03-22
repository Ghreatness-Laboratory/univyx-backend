from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    timezone = models.CharField(
        max_length=50,
        choices=[(tz, tz) for tz in timezone.all_timezones],
        default='UTC'
    )
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/events/%Y/%m/%d')
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
    date_created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.start_time and self.end_time and self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        if self.is_recurring and not self.recurrence_pattern:
            raise ValidationError("Please select a recurrence pattern for recurring events.")
        if not self.is_recurring:
            self.recurrence_pattern = None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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




# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     date = models.DateField(null=True, blank=True)
#     start_time = models.TimeField(null=True, blank=True)
#     end_time = models.TimeField(null=True, blank=True)
#     timezone = models.CharField(
#         max_length=50,
#         choices=[(tz, tz) for tz in timezone.all_timezones],
#         default='UTC'
#     )
#     location = models.CharField(max_length=250)
#     description = models.TextField()
#     image = models.ImageField(upload_to='uploads/events/%Y/%m/%d')
#     is_recurring = models.BooleanField(default=False)
#     recurrence_pattern = models.CharField(
#         max_length=20,
#         choices=[
#             ('daily', 'Daily'),
#             ('weekly', 'Weekly'),
#             ('monthly', 'Monthly'),
#             ('yearly', 'Yearly')
#         ],
#         blank=True,
#         null=True
#     )
#     date_created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

#     def __str__(self):
#         return self.title

#     @property
#     def time_range(self):
#         if self.start_time and self.end_time:
#             return f"{self.start_time.strftime('%I:%M%p').lower()} - {self.end_time.strftime('%I:%M%p').lower()}"
#         elif self.start_time:
#             return self.start_time.strftime('%I:%M%p').lower()
#         return ""

#     class Meta:
#         ordering = ['-date_created']
#         verbose_name = "Event"
#         verbose_name_plural = "Events"
