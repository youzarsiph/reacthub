""" API endpoints for untitled.stories """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.stories.models import Story, User
from untitled.stories.serializers import StorySerializer


# Create your views here.
class StoryViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete stories"""

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user"]


class UserStoriesViewSet(StoryViewSet):
    """Stories of a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        user = User.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(user=user)
