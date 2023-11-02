""" Serializers for untitled.stories """


from rest_framework.serializers import ModelSerializer
from untitled.stories.models import Story


# Create your serializers here.
class StorySerializer(ModelSerializer):
    """Story Serializer"""

    class Meta:
        """Meta data"""

        model = Story
        read_only_fields = []
        fields = []
