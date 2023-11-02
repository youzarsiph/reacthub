""" API endpoints for untitled.communities """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.communities.models import Community
from untitled.communities.serializers import CommunitySerializer


# Create your views here.
class CommunityViewSet(ModelViewSet):
    """Create, read, update and delete communities"""

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
