from django.db import models
from bands.models import Band
from songs.models import Song

# Create your models here.
class Concert(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='concerts')
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    date = models.DateField()
    tour_name = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.band.name} at {self.venue} ({self.date})"

    class Meta:
        ordering = ['-date']

class SetlistEntry(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='setlist')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    encore = models.BooleanField(default=False)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['order']
        unique_together = ('concert', 'order')

    def __str__(self):
        return f"{self.order}. {self.song.title}"
