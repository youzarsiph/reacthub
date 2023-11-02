""" URLConf for untitled.reports """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.reports.views import ReportViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reports", ReportViewSet, "report")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("reports/<int:id>/", include(sub_router.urls)),
]
