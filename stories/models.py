""" Data Models for untitled.stories """


from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Story(models.Model):
    """Stories"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    text = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        help_text="Text",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Image",
        upload_to="files/images/stories/",
    )
    video = models.FileField(
        null=True,
        blank=True,
        help_text="video",
        upload_to="files/videos/stories/",
        validators=[
            validators.FileExtensionValidator(["mp4"], "This file is not a video.")
        ],
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
