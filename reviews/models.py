""" Data Models for untitled.reviews """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Review(models.Model):
    """Reviews"""

    pass
