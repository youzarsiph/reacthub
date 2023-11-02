""" Mixins for untitled """


# Create your mixins here.
class OwnerMixin:
    """Adds the user field to a model automatically."""

    def perform_create(self, serializer):
        """Save the model with request.user"""

        serializer.save(user=self.request.user)
