from rest_framework import viewsets, filters, status
from django_filters import rest_framework as django_filter
from rest_framework.response import Response

from ..models import Category
from ..permissions import IsStaffOrReadOnly
from ..serializers import CategorySerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly, ]
    filter_backends = (django_filter.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['id', 'title', 'parent__id']
    tag = ['Category']

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        child = self.queryset.filter(parent=category)
        category_serializer = self.serializer_class(category)
        child_serializer = self.serializer_class(child, many=True)
        return Response(
            {'category': category_serializer.data, 'sub_category': child_serializer.data},
            status.HTTP_200_OK
        )
