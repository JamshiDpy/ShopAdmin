from django.contrib import admin
from .models import Shop


class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    readonly_fields = ['created_at']


admin.site.register(Shop, ShopModelAdmin)
