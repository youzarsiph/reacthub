""" URLConf for untitled.followers """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.followers.views import FollowerViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("followers", FollowerViewSet, "follower")


urlpatterns = [
    path("", include(router.urls)),
]
