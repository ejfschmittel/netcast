from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField( max_length=16)
    slug = models.SlugField(max_length=16)
    

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


