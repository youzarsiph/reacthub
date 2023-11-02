""" Serializers for untitled.pages """


from rest_framework.serializers import ModelSerializer
from untitled.pages.models import Page


# Create your serializers here.
class PageSerializer(ModelSerializer):
    """Page Serializer"""

    class Meta:
        """Meta data"""

        model = Page
        read_only_fields = []
        fields = []
