from django.contrib import admin
from .models import Bom

# Register your models here.

class BomAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'workstation_id', 'production_rate', 'created_at', 'update_at')

admin.site.register(Bom, BomAdmin)