from django.db import models
from podcasts.models import Podcast
# Create your models here.

from personalities.models import Personality

class Episode(models.Model):
    title = models.CharField(max_length=127)
    episode_num = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateField(null=True, blank=True)

    personalities = models.ManyToManyField(Personality, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    youtube_id = models.CharField(max_length=11, blank=True)
    spotify_id = models.CharField(max_length=11, blank=True)
    apple_id = models.CharField(max_length=13, blank=True)
    
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"

    def __str__(self):
        return self.title


