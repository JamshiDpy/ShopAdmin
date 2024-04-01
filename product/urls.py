from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet, 'category')
router.register('product_image', ProductImageViewSet, 'product_images')
router.register('', ProductViewSet, 'product')


urlpatterns = [
    path('', include(router.urls))
]