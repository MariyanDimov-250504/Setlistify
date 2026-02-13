from django.db import models
from bands.models import Band

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='songs')
    lyrics_preview = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} – {self.band.name}"

    class Meta:
        ordering = ['title']