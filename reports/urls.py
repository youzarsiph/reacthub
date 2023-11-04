""" URLConf for untitled.reports """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.reports.views import ReportViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reports", ReportViewSet, "report")


urlpatterns = [
    path("", include(router.urls)),
]
