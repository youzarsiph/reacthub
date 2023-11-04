""" API endpoints for untitled.reviews """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.pages.models import Page
from untitled.reviews.models import Review
from untitled.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["comment"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "page", "rating"]


class PageReviewsViewSet(ReviewViewSet):
    """Reviews of a page"""

    def perform_create(self, serializer):
        """Creates a review"""

        page = Page.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, page=page)

    def get_queryset(self):
        """Filter queryset by page"""

        page = Page.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(page=page)


class UserReviewsViewSet(ReviewViewSet):
    """Reviews created by a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
