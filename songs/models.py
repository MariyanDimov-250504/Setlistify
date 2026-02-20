from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from bands.models import Band

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        help_text="Year the song was released.",
        null=True,
        blank=True
    )
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='songs')
    lyrics_preview = models.TextField(blank=True)

    def duration_formatted(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.title} – {self.band.name}"

    class Meta:
        ordering = ['title']
