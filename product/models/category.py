import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True)

    def __str__(self):
        return  self.title
