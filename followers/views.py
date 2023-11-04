""" API endpoints for untitled.followers """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.followers.models import Follower
from untitled.followers.serializers import FollowerSerializer
from untitled.pages.models import Page


# Create your views here.
class FollowerViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete members"""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "user__first_name", "user__last_name"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "page", "is_admin", "is_banned"]


class PageFollowersViewSet(FollowerViewSet):
    """Followers of a pge"""

    def perform_create(self, serializer):
        """Creates a follower"""

        page = Page.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, page=page)

    def get_queryset(self):
        """Filter queryset by page"""

        page = Page.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(page=page)


class UserFollowersViewSet(FollowerViewSet):
    """Followers filtered by user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
