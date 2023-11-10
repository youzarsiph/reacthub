""" URLConf for untitled.friends """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.friends.views import UserFriendsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("friends", UserFriendsViewSet, "friend")


urlpatterns = [
    path("", include(router.urls)),
]
