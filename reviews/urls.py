""" URLConf for untitled.reviews """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.reviews.views import ReviewViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reviews", ReviewViewSet, "review")


urlpatterns = [
    path("", include(router.urls)),
]
