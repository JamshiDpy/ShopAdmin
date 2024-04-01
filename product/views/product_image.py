from rest_framework import viewsets

from product.models import ProductImage
from product.serializers import ProductImageSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Product_image'])
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
