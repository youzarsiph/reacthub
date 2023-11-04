""" Serializers for untitled.comments """


from rest_framework.serializers import ModelSerializer
from untitled.comments.models import Comment


# Create your serializers here.
class CommentSerializer(ModelSerializer):
    """Comment Serializer"""

    class Meta:
        """Meta data"""

        model = Comment
        read_only_fields = ["user", "post"]
        fields = [
            "id",
            "url",
            "user",
            "post",
            "text",
            "image",
            "replies",
            "created_at",
            "updated_at",
        ]
