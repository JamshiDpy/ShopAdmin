from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, permissions, status, mixins
from rest_framework.response import Response
from .permissions import UserCreatePermission
from .serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
    queryset = None
    serializer_class = RegistrationSerializer
    permission_classes = [UserCreatePermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(username=serializer.validated_data['username'],
                                   user_type='product_admin',
                                   is_staff=True)
        user.set_password(serializer.validated_data['password1'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class AdminViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserCreatePermission, ]
