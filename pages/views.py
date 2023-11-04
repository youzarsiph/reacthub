""" API endpoints for untitled.pages """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.pages.models import Page
from untitled.pages.serializers import PageSerializer


# Create your views here.
class PageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete pages"""

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "name"]
