from rest_framework import serializers

from .models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'image']

        extra_kwargs = {'image': {'read_only': False}}


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'description', 'image', 'created_at']

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True}
        }
