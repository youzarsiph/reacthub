""" Data Models for untitled.reviews """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Review(models.Model):
    """Reviews"""

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
    rating = models.SmallIntegerField(
        default=1,
        help_text="Rating",
        choices=[
            (1, "Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
    )
    comment = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Your Comment",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["user", "page"],
                name="unique_review_user_page",
            )
        ]

    def __str__(self) -> str:
        return super().__str__()
