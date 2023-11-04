""" Data Models for untitled.pages """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Page(models.Model):
    """Pages"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pages",
        help_text="Page Owner",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Page Photo",
        upload_to="files/images/pages/",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        help_text="Page Cover Photo",
        upload_to="files/images/pages/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Page Name",
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Page Description",
    )
    followers = models.ManyToManyField(
        User,
        through="followers.Follower",
        help_text="Page Followers",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
