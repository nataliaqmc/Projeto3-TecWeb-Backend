from django.db import models


class Music(models.Model):
    #title = models.CharField(max_length=200)
    song = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)
    def __str__(self):
        return str(self.id) + ". " + self.song
    