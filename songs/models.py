from django.db import models
from django.utils import timezone

class Song(models.Model):
    MOOD_CHOICES = [
        ('chill', 'Chill'),
        ('romantic', 'Romantic'),
        ('heartbreak', 'Heartbreak'),
        ('soulful', 'Soulful'),
        ('classic', 'Classic'),
        ('old-but-gold', 'Old But Gold'),
    ]

    LANGUAGE_CHOICES = [
        ('hindi', 'Hindi'),
    ]

    title = models.CharField(max_length=255)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='hindi')
    description = models.TextField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='song_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
