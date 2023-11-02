""" Data Models for untitled """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Untitled Users"""

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/users/",
        help_text="User profile photo",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/users/covers/",
        help_text="User profile cover photo",
    )
    about = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="About yourself",
    )
