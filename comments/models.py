""" Data Models for untitled.comments """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Comment(models.Model):
    """Comments"""

    pass
