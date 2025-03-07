from django.db import models

import math

class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ("technology", "Technology"),
        ("business", "Business"),
        ("sports", "Sports"),
        ("entertainment", "Entertainment"),
        ("health", "Health"),
        ("politics", "Politics"),
        ("science", "Science"),
        ("world", "World"),
        ("other", "Other"),
    ]

    SECTION_CHOICES = [
        ("featured", "Featured"),
        ("trending", "Trending"),
        ("latest", "Latest"),
        ("opinion", "Opinion"),
        ("editorial", "Editorial"),
    ]

    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.URLField()
    likes = models.PositiveIntegerField(default=0)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    content = models.TextField(blank=True, null=True)
    read_time = models.PositiveIntegerField(default=1)  # Stored in DB

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def calculate_read_time(self):
        """
        Recalculates and updates read time based on word count.
        Did you know: The average human reads 200 words per min
        time taken to read = 

        """
        words = len(self.content.split()) if self.content else 0
        self.read_time = max(1, math.ceil(words / 200))  # Ensure at least 1 min
        self.save(update_fields=["read_time"])

    @property
    def estimated_read_time(self):
        """Returns stored read time but recalculates if missing."""
        if not self.read_time or self.read_time == 1:
            self.calculate_read_time()
        return f"{self.read_time} min read"

    def save(self, *args, **kwargs):
        """Automatically updates read time when content changes."""
        if self.pk:
            old_instance = NewsArticle.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.content != self.content:
                self.calculate_read_time()
        super().save(*args, **kwargs)

