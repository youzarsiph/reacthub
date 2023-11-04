""" URLConf for untitled.members """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.members.views import MemberViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("members", MemberViewSet, "story")


urlpatterns = [
    path("", include(router.urls)),
]
