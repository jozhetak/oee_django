from django.contrib import admin
from .models import JobOrder

# Register your models here.

class JobOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_number', 'item','job_status', 'planned_qty', 'cmplt_qty', 'batch_number', 'due_date', 'created_at', 'update_at')

admin.site.register(JobOrder, JobOrderAdmin)