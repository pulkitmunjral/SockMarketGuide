from django.db import models
from embed_video.fields import EmbedVideoField


class Stock(models.Model):    
    title = models.CharField(max_length=50)    
    desc = models.CharField(max_length=300, blank=True, null=True)
    video = EmbedVideoField()

    def __str__(self) -> str:        
        return str(self.title)


class Query(models.Model):
    username = models.CharField(max_length=50)
    stockname = models.CharField(max_length=50)
    query = models.CharField(max_length=300, blank=True, null=True)
