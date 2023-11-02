""" API endpoints for untitled.reviews """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.reviews.models import Review
from untitled.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(ModelViewSet):
    """Create, read, update and delete reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
