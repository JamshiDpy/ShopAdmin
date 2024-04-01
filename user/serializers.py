from rest_framework import serializers
from django.contrib.auth import get_user_model

# from django

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=8, max_length=32)
    password2 = serializers.CharField(min_length=8, max_length=32)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']

    def validate(self, attrs):
        password1 = attrs['password1']
        password2 = attrs['password2']
        if password1 != password2:
            raise serializers.ValidationError("Password fields do not match")
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_type']

        extra_kwargs = {
            'id': {'read_only': True}
        }
