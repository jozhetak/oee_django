from django.contrib import admin
from .models import Plant

# Register your models here.

class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant_name', 'created_at', 'update_at')

admin.site.register(Plant, PlantAdmin)
