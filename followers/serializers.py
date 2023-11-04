""" Serializers for untitled.followers """


from rest_framework.serializers import ModelSerializer
from untitled.followers.models import Follower


# Create your serializers here.
class FollowerSerializer(ModelSerializer):
    """Follower Serializer"""

    class Meta:
        """Meta data"""

        model = Follower
        read_only_fields = ["user", "page"]
        fields = [
            "id",
            "url",
            "user",
            "page",
            "is_admin",
            "is_banned",
            "created_at",
            "updated_at",
        ]
