""" API endpoints for untitled.reports """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.reports.models import Report
from untitled.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(ModelViewSet):
    """Create, read, update and delete reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
