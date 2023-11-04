""" Data Models for untitled.posts """


from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Post(models.Model):
    """Posts"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="Post Owner",
    )
    community = models.ForeignKey(
        "communities.Community",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
        help_text="Community",
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
        help_text="Page",
    )
    text = models.TextField(
        null=True,
        blank=True,
        help_text="Post Text",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Community Photo",
        upload_to="files/images/posts/",
    )
    video = models.FileField(
        null=True,
        blank=True,
        help_text="video",
        upload_to="files/videos/stories/",
        validators=[
            validators.FileExtensionValidator(
                ["mp4"],
                "This file is not a video.",
            ),
        ],
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text="File",
        upload_to="files/posts/",
    )
    is_pinned = models.BooleanField(
        default=False,
        help_text="Designates if the post is pinned",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
