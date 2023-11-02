""" URLConf for untitled.pages """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.pages.views import PageViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("pages", PageViewSet, "page")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("pages/<int:id>/", include(sub_router.urls)),
]
