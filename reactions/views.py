""" API endpoints for untitled.reactions """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.reactions.models import Reaction
from untitled.reactions.serializers import ReactionSerializer


# Create your views here.
class ReactionViewSet(ModelViewSet):
    """Create, read, update and delete reactions"""

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
