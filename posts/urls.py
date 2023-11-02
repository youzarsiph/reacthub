""" URLConf for untitled.posts """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.posts.views import PostViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("posts", PostViewSet, "post")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:id>/", include(sub_router.urls)),
]
