from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class GeneralUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(null=True)

    @staticmethod
    def is_user_admin(user_id):
        try:
            user = GeneralUser.objects.get(id=user_id)
            return user.isAdmin
        except ObjectDoesNotExist:
            return False


class User(GeneralUser):

    def __str__(self):
        return self.username


class Admin(GeneralUser):

    def __str__(self):
        return self.username
