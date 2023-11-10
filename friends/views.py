""" API endpoints for untitled.friends """


from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.friends.models import Friend
from untitled.friends.serializers import FriendSerializer


# Create your views here.
class FriendViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete friends"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]
    search_fields = [
        "from_user__username",
        "from_user__first_name",
        "from_user__last_name",
        "to_user__username",
        "to_user__first_name",
        "to_user__last_name",
    ]
    ordering_fields = ["created_at"]
    filterset_fields = ["from_user", "to_user", "is_accepted", "is_blocked"]


class UserFriendsViewSet(FriendViewSet):
    """Friends of a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        )
