from django.db import models

import math

class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ('all','ALL'),
        ('environment','Environment'),
        ('campus','Campus'),
        ('sports','Sports'),
        ('academics','Academics'),
        ('research','Research')
    ]

    title = models.CharField(max_length=255)
    # source 
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True,null=True, editable=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='uploads/news_img', null=True)
    likes = models.PositiveIntegerField(default=0, editable=False) # implement websocket
    # section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    content = models.TextField(blank=True, null=True)
    read_time = models.CharField(max_length=50,blank=True, editable=False)  # Stored in DB

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def calculate_read_time(self):
        """
        Recalculates and updates read time based on word count.
        Did you know: The average human reads 200 words per min
        time taken to read = 

        """
        words_per_minute = 200
        total_words = len(self.content.split()) if self.content else 0
        read_time_minutes = total_words / words_per_minute
        read_time_second = math.ceil(read_time_minutes * 60)

        if read_time_second < 60:
            return f"{read_time_second} sec"
        else: 
            return f"{math.ceil(read_time_minutes)} min"

        # self.read_time = max(1, math.ceil(words / 200))  # Ensure at least 1 min
        # return self.read_time
        # self.save(update_fields=["read_time"])

    @property
    def estimated_read_time(self):
        """Returns stored read time but recalculates if missing."""
        if not self.read_time or self.read_time == 1:
            self.calculate_read_time()
        return self.calculate_read_time()

    def generate_detail(self):
        return self.content[:100] + "..." if len(self.content) < 100 else self.content

    def save(self, *args, **kwargs):
        """Automatically updates read time when content changes."""
        if self.pk:
            old_instance = NewsArticle.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.content != self.content:
                self.read_time = self.calculate_read_time()
                self.description = self.generate_detail()
        else:
            self.read_time = self.calculate_read_time()
            self.description = self.generate_detail()
        super().save(*args, **kwargs)

