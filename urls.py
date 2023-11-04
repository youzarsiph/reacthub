""" URLConf for untitled """


from django.urls import path, include


# Create your URLConf here.
urlpatterns = [
    # Comments
    path("", include("untitled.comments.urls")),
    # Communities
    path("", include("untitled.communities.urls")),
    # Followers
    path("", include("untitled.followers.urls")),
    # Members
    path("", include("untitled.members.urls")),
    # Pages
    path("", include("untitled.pages.urls")),
    # Pages
    path("", include("untitled.pages.urls")),
    # Reactions
    path("", include("untitled.reactions.urls")),
    # Reports
    path("", include("untitled.reports.urls")),
    # Reviews
    path("", include("untitled.reviews.urls")),
    # Stories
    path("", include("untitled.stories.urls")),
]
