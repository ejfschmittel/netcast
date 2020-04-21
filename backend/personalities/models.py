from django.db import models

# Create your models here.

class Personality(models.Model):
    firstname = models.CharField(max_length=31)
    lastname = models.CharField(max_length=31)
    displayname = models.CharField(max_length=31)

    bio = models.TextField()

    # options birthdate, social media

    class Meta:
        verbose_name = "Personality"
        verbose_name_plural = "Personalities"

    def __str__(self):
        return self.firstname + " " + self.lastname