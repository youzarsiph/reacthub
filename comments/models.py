""" Data Models for untitled.comments """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Comment(models.Model):
    """Comments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="Comment Owner",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="Commented Post",
    )
    text = models.TextField(
        null=True,
        blank=True,
        help_text="Comment Text",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Image",
    )
    replies = models.ManyToManyField(
        "self",
        help_text="Comment Replies",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
