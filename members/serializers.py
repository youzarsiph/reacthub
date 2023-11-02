""" Serializers for untitled.members """


from rest_framework.serializers import ModelSerializer
from untitled.members.models import Member


# Create your serializers here.
class MemberSerializer(ModelSerializer):
    """Member Serializer"""

    class Meta:
        """Meta data"""

        model = Member
        read_only_fields = []
        fields = []
