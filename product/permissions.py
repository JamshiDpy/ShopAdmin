from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsProductAdminAndSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            return request.user.user_type == 'product-admin' or request.user.is_superuser

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
