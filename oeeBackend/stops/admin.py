from django.contrib import admin
from .models import Stop

# Register your models here.

class StopAdmin(admin.ModelAdmin):
    list_display = ('id', 'stop_name', 'stop_type', 'stop_res_email')


admin.site.register(Stop, StopAdmin)