from django.db import models


class Stock(models.Model):    
    title = models.CharField(max_length=50)    
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:        
        return self.title