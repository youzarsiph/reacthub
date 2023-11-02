""" Serializers for untitled.communities """


from rest_framework.serializers import ModelSerializer
from untitled.communities.models import Community


# Create your serializers here.
class CommunitySerializer(ModelSerializer):
    """Community Serializer"""

    class Meta:
        """Meta data"""

        model = Community
        read_only_fields = []
        fields = []
