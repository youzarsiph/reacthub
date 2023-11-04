""" URLConf for untitled.stories """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.stories.views import StoryViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("stories", StoryViewSet, "story")


urlpatterns = [
    path("", include(router.urls)),
]
