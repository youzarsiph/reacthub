""" URLConf for untitled.posts """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.comments.views import PostCommentsViewSet
from untitled.posts.views import PostViewSet
from untitled.reactions.views import PostReactionsViewSet
from untitled.reports.views import PostReportsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("posts", PostViewSet, "post")

sub_router = DefaultRouter()
sub_router.register("comments", PostCommentsViewSet, "comment")
sub_router.register("reactions", PostReactionsViewSet, "reaction")
sub_router.register("reports", PostReportsViewSet, "report")

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:id>/", include((sub_router.urls, "posts"), namespace="posts")),
]
