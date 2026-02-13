from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=200, unique=True)
    formed_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']