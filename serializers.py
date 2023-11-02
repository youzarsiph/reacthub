""" Serializers for untitled """


from rest_framework.serializers import ModelSerializer
from untitled.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = ["id", "url", "username", "first_name", "last_name"]
