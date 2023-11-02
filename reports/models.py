""" Data Models for untitled.reports """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Report(models.Model):
    """Reports"""

    pass
