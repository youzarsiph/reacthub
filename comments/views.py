""" API endpoints for untitled.comments """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.comments.models import Comment
from untitled.comments.serializers import CommentSerializer


# Create your views here.
class CommentViewSet(ModelViewSet):
    """Create, read, update and delete comments"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
