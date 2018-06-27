from django.contrib import admin
from .models import JobOrderDetail

# Register your models here.

class JobOrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_order', 'item', 'workstation', 'production_rate',
                    'created_at', 'update_at')

admin.site.register(JobOrderDetail, JobOrderDetailAdmin)