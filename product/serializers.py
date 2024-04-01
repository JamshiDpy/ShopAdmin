import uuid

from rest_framework import serializers

from product.models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'parent']

        extra_kwargs = {
            'id': {'read_only': True},
            'parent': {'required': False}
        }


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', ]


class ProductCreateSerializer(serializers.ModelSerializer):
    upload_images = serializers.ListField(
        child=serializers.ImageField(allow_null=False, use_url=False, write_only=True)
    )

    class Meta:
        model = Product
        fields = ['category',
                  'shop',
                  'name',
                  'description',
                  'amount',
                  'price',
                  'upload_images',
                  'active', ]


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'shop',
            'name',
            'description',
            'amount',
            'price',
            'image',
            'active',
            'number_of_orders'
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'number_of_orders': {'read_only': True},
        }

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['image'] = ProductImageSerializer(instance.image.all(), many=True).data
    #     return data
