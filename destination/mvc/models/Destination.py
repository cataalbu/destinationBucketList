from django.db import models


class Destination(models.Model):
    geolocation = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    user_id = models.PositiveIntegerField(null=True)
    is_public = models.BooleanField()

    def __str__(self):
        return self.title + self.description
