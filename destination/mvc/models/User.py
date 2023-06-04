from django.db import models

# Create your models here.


class GeneralUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(null=True)


class User(GeneralUser):

    def __str__(self):
        return self.username


class Admin(GeneralUser):

    def __str__(self):
        return self.username
