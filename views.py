""" API endpoints for untitled """


from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from untitled.models import User
from untitled.permissions import IsAccountOwner
from untitled.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """Create, read, update and delete stories"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["date_joined"]
    filterset_fields = ["username"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "delete"]:
            self.permission_classes += [IsAccountOwner]

        return super().get_permissions()
