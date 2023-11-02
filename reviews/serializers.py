""" Serializers for untitled.reviews """


from rest_framework.serializers import ModelSerializer
from untitled.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(ModelSerializer):
    """Review Serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = []
        fields = []
