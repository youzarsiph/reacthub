""" Data Models for untitled.members """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Member(models.Model):
    """Community Members"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    community = models.ForeignKey(
        "communities.Community",
        on_delete=models.CASCADE,
        help_text="Community",
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates if this member is an admin.",
    )
    is_banned = models.BooleanField(
        default=False,
        help_text="Designates if this member is banned.",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["user", "community"],
                name="unique_member_user_community",
            )
        ]
