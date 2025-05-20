from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    location = models.CharField(max_length=255)
    rooms = models.IntegerField()          
    area = models.FloatField()             
    floor = models.IntegerField()          
    image_url = models.URLField(blank=True) 

    def __str__(self):
        return self.title
