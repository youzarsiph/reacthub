""" Data Models for untitled.reports """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Report(models.Model):
    """Reports"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    community = models.ForeignKey(
        "communities.Community",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Community",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Post",
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Page",
    )
    comment = models.CharField(
        max_length=64,
        help_text="What is the problem?",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
