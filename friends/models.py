""" Data Models for untitled.friends """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Friend(models.Model):
    """Friends"""

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="from_user",
        help_text="Requested by",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="to_user",
        help_text="Accepted by",
    )
    is_accepted = models.BooleanField(
        default=False,
        help_text="Designates if friends request is accepted.",
    )
    is_blocked = models.BooleanField(
        default=False,
        help_text="Designates if this friend is blocked.",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["from_user", "to_user"],
                name="unique_friend_from_user_to_user",
            )
        ]
