from django.db import models

# Create your models here.


class Destination(models.Model):
    geolocation = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    user_id = models.PositiveIntegerField(null=True)
    is_public = models.BooleanField()

    def __str__(self):
        return self.title + self.description


class GeneralUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class User(GeneralUser):

    def __str__(self):
        return self.username


class Admin(GeneralUser):

    def __str__(self):
        return self.username
