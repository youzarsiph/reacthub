""" API endpoints for untitled.posts """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.posts.models import Post
from untitled.posts.serializers import PostSerializer


# Create your views here.
class PostViewSet(ModelViewSet):
    """Create, read, update and delete posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
