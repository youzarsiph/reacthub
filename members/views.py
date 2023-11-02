""" API endpoints for untitled.members """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.members.models import Member
from untitled.members.serializers import MemberSerializer


# Create your views here.
class MemberViewSet(ModelViewSet):
    """Create, read, update and delete members"""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
