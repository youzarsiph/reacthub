""" API endpoints for untitled.reactions """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.posts.models import Post
from untitled.reactions.models import Reaction
from untitled.reactions.serializers import ReactionSerializer


# Create your views here.
class ReactionViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete reactions"""

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["value"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "post", "value"]


class PostReactionsViewSet(ReactionViewSet):
    """Reactions of a post"""

    def perform_create(self, serializer):
        """Creates a reaction"""

        post = Post.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        """Filter queryset by post"""

        post = Post.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(post=post)


class UserReactionsViewSet(ReactionViewSet):
    """Reactions of a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
