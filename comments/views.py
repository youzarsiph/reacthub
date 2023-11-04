""" API endpoints for untitled.comments """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.comments.models import Comment
from untitled.comments.serializers import CommentSerializer
from untitled.posts.models import Post


# Create your views here.
class CommentViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete comments"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "post"]


class PostCommentsViewSet(CommentViewSet):
    """Comments of a post"""

    def perform_create(self, serializer):
        """Perform comment creation"""

        post = Post.object.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        """Filter queryset by post"""

        post = Post.object.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(post=post)


class UserCommentsViewSet(CommentViewSet):
    """Comments of a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
