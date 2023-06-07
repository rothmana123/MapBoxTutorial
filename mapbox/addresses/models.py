import geocoder

from django.db import models

# Create your models here.

access_token = 'pk.eyJ1IjoiYXNyb3RobWFuMSIsImEiOiJjbGlrZTA4ODkwNHpoM3ZxazZ0anY5aXpiIn0.HIGJLTOaPjurO6zhhiQKAQ'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

