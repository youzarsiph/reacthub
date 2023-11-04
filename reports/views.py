""" API endpoints for untitled.reports """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.communities.models import Community
from untitled.pages.models import Page
from untitled.reports.models import Report
from untitled.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["comment"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "community", "post", "page"]


class CommunityReportsViewSet(ReportViewSet):
    """Reports of a community"""

    def perform_create(self, serializer):
        """Creates a community report"""

        community = Community.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, community=community)

    def get_queryset(self):
        """Filter queryset by community"""

        community = Community.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(community=community)


class PageReportsViewSet(ReportViewSet):
    """Reports of a page"""

    def perform_create(self, serializer):
        """Creates a page report"""

        page = Page.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, page=page)

    def get_queryset(self):
        """Filter queryset by page"""

        page = Page.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(page=page)


class UserReportsViewSet(ReportViewSet):
    """Reports created by a user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
