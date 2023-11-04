""" URLConf for untitled.communities """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.communities.views import CommunityViewSet
from untitled.members.views import CommunityMembersViewSet
from untitled.posts.views import CommunityPostsViewSet
from untitled.reports.views import CommunityReportsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("communities", CommunityViewSet, "community")

sub_router = DefaultRouter()
sub_router.register("members", CommunityMembersViewSet, "member")
sub_router.register("posts", CommunityPostsViewSet, "post")
sub_router.register("reports", CommunityReportsViewSet, "report")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "communities/<int:id>/",
        include((sub_router.urls, "communities"), namespace="communities"),
    ),
]
