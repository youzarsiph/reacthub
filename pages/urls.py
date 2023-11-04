""" URLConf for untitled.pages """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.pages.views import PageViewSet
from untitled.followers.views import PageFollowersViewSet
from untitled.posts.views import PagePostsViewSet
from untitled.reports.views import PageReportsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("pages", PageViewSet, "page")

sub_router = DefaultRouter()
sub_router.register("followers", PageFollowersViewSet, "follower")
sub_router.register("posts", PagePostsViewSet, "post")
sub_router.register("reports", PageReportsViewSet, "report")

urlpatterns = [
    path("", include(router.urls)),
    path("pages/<int:id>/", include((sub_router.urls, "pages"), namespace="pages")),
]
