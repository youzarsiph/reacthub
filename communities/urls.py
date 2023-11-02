""" URLConf for untitled.communities """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.communities.views import CommunityViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("communities", CommunityViewSet, "community")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("communities/<int:id>/", include(sub_router.urls)),
]
