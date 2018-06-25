from django.contrib import admin
from .models import JobOrderData

# Register your models here.

class JobOrderDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_number_id', 'shift_id', 'job_partial_status', 'packaged_qty',
                    'retention_samples_qty', 'reworked_qty', 'q_issues_qty', 'rejected_qty',
                    'first_pass_qty', 'total_qty', 'job_process_time', 'planned_downtime',
                    'not_planned_downtime', 'start_datetime', 'close_datetime', 'workstation', 'job_performance_comments', 'job_quality_comments',
                    'created_at', 'update_at')

admin.site.register(JobOrderData, JobOrderDataAdmin)