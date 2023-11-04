""" Serializers for untitled.reactions """


from rest_framework.serializers import ModelSerializer
from untitled.reactions.models import Reaction


# Create your serializers here.
class ReactionSerializer(ModelSerializer):
    """Reaction Serializer"""

    class Meta:
        """Meta data"""

        model = Reaction
        read_only_fields = ["user", "post"]
        fields = ["id", "url", "user", "post", "value", "created_at", "updated_at"]
