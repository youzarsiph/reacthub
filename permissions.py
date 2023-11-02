""" Permissions for untitled """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Allow access only to owner of the object."""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
