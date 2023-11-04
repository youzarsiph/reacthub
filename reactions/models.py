""" Data Models for untitled.reactions """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Reaction(models.Model):
    """Post Reactions"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        help_text="Post",
    )
    value = models.CharField(
        max_length=32,
        help_text="Reaction",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_reaction_user_post",
            )
        ]

    def __str__(self) -> str:
        return super().__str__()
