from rest_framework.permissions import BasePermission


class UserCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
