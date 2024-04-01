import uuid

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    class UserType(models.TextChoices):
        ProductAdmin = 'product_admin'
        ShopAdmin = 'shop_admin'

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    first_name = None
    last_name = None
    user_type = models.CharField(max_length=100, choices=UserType)


