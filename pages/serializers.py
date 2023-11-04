""" Serializers for untitled.pages """


from rest_framework.serializers import ModelSerializer
from untitled.pages.models import Page


# Create your serializers here.
class PageSerializer(ModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Page
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "cover",
            "name",
            "description",
            "followers",
            "created_at",
            "updated_at",
        ]
