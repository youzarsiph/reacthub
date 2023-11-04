""" API endpoints for untitled.posts """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.communities.models import Community
from untitled.pages.models import Page
from untitled.posts.models import Post
from untitled.posts.serializers import PostSerializer


# Create your views here.
class PostViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "community", "page", "post"]


class CommunityPostsViewSet(PostViewSet):
    """Posts of a community"""

    def perform_create(self, serializer):
        """Creates a post in a community"""

        community = Community.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, community=community)

    def get_queryset(self):
        """Filter queryset by community"""

        community = Community.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(community=community)


class PagePostsViewSet(PostViewSet):
    """Posts of a page"""

    def perform_create(self, serializer):
        """Creates a post in a page"""

        page = Page.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, page=page)

    def get_queryset(self):
        """Filter queryset by page"""

        page = Page.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(page=page)


class UserPostsViewSet(PostViewSet):
    """Posts of a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
