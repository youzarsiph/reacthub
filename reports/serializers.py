""" Serializers for untitled.reports """


from rest_framework.serializers import ModelSerializer
from untitled.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report Serializer"""

    class Meta:
        """Meta data"""

        model = Report
        read_only_fields = ["user", "community", "post", "page"]
        fields = [
            "id",
            "url",
            "user",
            "community",
            "post",
            "page",
            "comment",
            "created_at",
            "updated_at",
        ]
