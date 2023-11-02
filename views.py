""" API endpoints for untitled """


from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from untitled.models import User
from untitled.serializers import UserSerializer


# Create your views here.
class StoryViewSet(ModelViewSet):
    """Create, read, update and delete stories"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
