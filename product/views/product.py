from django.db import models
from rest_framework import viewsets, status, filters, parsers
from rest_framework.response import Response

from ..models import Product, ProductImage
from ..serializers import ProductSerializer, ProductCreateSerializer
from ..permissions import IsProductAdminAndSuperUserOrReadOnly

from django_filters import FilterSet, RangeFilter, rest_framework as django_filters


class ProductFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'active']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    permission_classes = [IsProductAdminAndSuperUserOrReadOnly, ]
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['id', 'name']
    # filterset_fields = ['price', 'active']
    ordering_fields = ['number_of_orders', 'price']

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = ProductCreateSerializer
        else:
            self.serializer_class = ProductSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        images = serializer.validated_data.pop('upload_images')
        product = Product.objects.create(**serializer.validated_data)
        for img in images:
            image = ProductImage.objects.create(image=img)
            product.image.add(image)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_201_CREATED)


