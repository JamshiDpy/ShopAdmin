from django.db import models


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product')
