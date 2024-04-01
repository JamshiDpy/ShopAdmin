import uuid

from django.db import models
from .image import ProductImage
from .category import Category
from shop.models import Shop


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    category = models.ForeignKey(Category, models.CASCADE)
    shop = models.ForeignKey(Shop, models.CASCADE, related_name='product')
    name = models.CharField(max_length=250)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.FloatField()
    image = models.ManyToManyField(ProductImage)
    active = models.BooleanField(default=True)
    number_of_orders = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def main_image(self):
        image = self.image.first()
        return image.image
