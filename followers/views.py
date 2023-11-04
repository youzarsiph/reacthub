""" API endpoints for untitled.followers """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.followers.models import Follower
from untitled.followers.serializers import FollowerSerializer


# Create your views here.
class FollowerViewSet(ModelViewSet):
    """Create, read, update and delete members"""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
