""" API endpoints for untitled.communities """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.communities.models import Community
from untitled.communities.serializers import CommunitySerializer


# Create your views here.
class CommunityViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete communities"""

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "name", "is_private"]
