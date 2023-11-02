""" URLConf for untitled.reactions """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.reactions.views import ReactionViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reactions", ReactionViewSet, "reaction")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("reactions/<int:id>/", include(sub_router.urls)),
]
