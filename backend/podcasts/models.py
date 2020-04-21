from django.db import models
from categories.models import Category
from personalities.models import Personality
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

User = get_user_model()

class Podcast(models.Model):
    #id = 
    name = models.CharField( max_length=127, blank=False, null=False)
    slug = models.SlugField(max_length=31, blank=True, null=True)
    description = models.TextField(blank=True)
    #brilliantidiots

    #episode_count = # how to incrment

    '''
    image 
    thumbnail
    '''
  

    
    youtube_page = models.URLField( max_length=127, blank=True, null=False)
    website = models.URLField( max_length=127, blank=True, null=False)
    apple_page = models.URLField( max_length=127, blank=True, null=False)
    spotify_page = models.URLField( max_length=127, blank=True, null=False)
    

    categories = models.ManyToManyField(Category)
    personalities = models.ManyToManyField(Personality)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL)
      

    class Meta:
        verbose_name = "podcast"
        verbose_name_plural = "podcasts"

    def __str__(self):
        return self.name

