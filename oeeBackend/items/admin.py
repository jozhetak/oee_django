from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_code', 'item_name', 'created_at', 'update_at')

admin.site.register(Item, ItemAdmin)
