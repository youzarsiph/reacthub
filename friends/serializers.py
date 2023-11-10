""" Serializers for untitled.friends """


from rest_framework.serializers import ModelSerializer
from untitled.friends.models import Friend


# Create your serializers here.
class FriendSerializer(ModelSerializer):
    """Friend Serializer"""

    class Meta:
        """Meta data"""

        model = Friend
        read_only_fields = ["from_user", "to_user"]
        fields = [
            "id",
            "url",
            "from_user",
            "to_page",
            "is_accepted",
            "is_blocked",
            "created_at",
            "updated_at",
        ]
