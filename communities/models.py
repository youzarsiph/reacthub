""" Data Models for untitled.communities """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Community(models.Model):
    """Communities"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="communities",
        help_text="Community Owner",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Community Photo",
        upload_to="files/images/communities/",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        help_text="Community Cover Photo",
        upload_to="files/images/communities/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Community Name",
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Community Description",
    )
    is_private = models.BooleanField(
        default=False,
        help_text="Designates if the community is private",
    )
    members = models.ManyToManyField(
        User,
        through="members.Member",
        help_text="Community Members",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
