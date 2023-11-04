""" Serializers for untitled.posts """


from rest_framework.serializers import ModelSerializer
from untitled.posts.models import Post


# Create your serializers here.
class PostSerializer(ModelSerializer):
    """Post Serializer"""

    class Meta:
        """Meta data"""

        model = Post
        read_only_fields = ["user", "community", "page", "is_pinned"]
        fields = [
            "id",
            "url",
            "user",
            "community",
            "page",
            "text",
            "photo",
            "video",
            "file",
            "is_pinned",
            "created_at",
            "updated_at",
        ]
