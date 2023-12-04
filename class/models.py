from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

class Item(models.Model):
    item = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)