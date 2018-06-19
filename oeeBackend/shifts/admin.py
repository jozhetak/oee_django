from django.contrib import admin
from shifts.models import Shift

# Register your models here.

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'shift_name', 'start_time', 'end_time', 'created_at', 'update_at')

admin.site.register(Shift, ShiftAdmin)
