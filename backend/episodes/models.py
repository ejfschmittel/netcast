from django.db import models
from podcasts.models import Podcast
# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(blank=True)
    upload_date = models.DateField()


    youtube_id = models.CharField(max_length=11)
    spotify_id = models.CharField(max_length=11)
    apple_id = models.CharField(max_length=13)
    
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"

    def __str__(self):
        return self.title


