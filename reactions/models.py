""" Data Models for untitled.reactions """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Reaction(models.Model):
    """Reactions"""

    pass
