""" Data Models for untitled.stories """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Story(models.Model):
    """Stories"""

    pass
