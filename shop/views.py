from rest_framework import viewsets, permissions, mixins, generics, status, parsers, filters
from rest_framework.response import Response

from .serializers import ShopSerializer, ShopCreateSerializer
from .models import Shop
from .permissions import IsSuperUserOrShopAdmin


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    parser_classes = [parsers.MultiPartParser]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [IsSuperUserOrShopAdmin, ]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            return ShopCreateSerializer
        return ShopSerializer
