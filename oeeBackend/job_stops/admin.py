from django.contrib import admin
from .models import JobStop

# Register your models here.

class JobStopAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_order_data_id', 'stop_id', 'start_datetime', 'close_datetime',
                    'stop_time', 'stop_type', 'stop_description', 'created_at', 'update_at')

admin.site.register(JobStop, JobStopAdmin)