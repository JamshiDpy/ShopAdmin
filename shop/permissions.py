from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrShopAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.user_type == 'shop_admin' or request.user.is_superuser
        return False
