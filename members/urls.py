""" URLConf for untitled.members """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.members.views import MemberViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("members", MemberViewSet, "story")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("members/<int:id>/", include(sub_router.urls)),
]
