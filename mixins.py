""" Mixins for untitled """


from untitled.permissions import IsOwner


# Create your mixins here.
class OwnerMixin:
    """Adds the user field to a model automatically."""

    def perform_create(self, serializer):
        """Save the model with request.user"""

        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "delete"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()
