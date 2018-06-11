from django.contrib import admin
from .models import Workstation

# Register your models here.

class WorkstationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ws_name', 'ws_type', 'ws_plant', 'created_at', 'update_at')

admin.site.register(Workstation, WorkstationAdmin)