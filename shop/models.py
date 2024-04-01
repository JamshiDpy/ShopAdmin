import uuid

from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Shop(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='shop', default='default_shop.png')
    created_at = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.name

