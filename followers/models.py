""" Data Models for untitled.followers """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Follower(models.Model):
    """Page Followers"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        help_text="Page",
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates if this follower is an admin.",
    )
    is_banned = models.BooleanField(
        default=False,
        help_text="Designates if this follower is banned.",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["user", "page"],
                name="unique_follower_user_page",
            )
        ]
