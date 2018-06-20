from django.contrib import admin
from .models import JobQualityIssue

# Register your models here.

class JobQualityIssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_order_data_id', 'q_issue_id', 'q_issue_qty', 'reworked', 'created_at', 'update_at')

admin.site.register(JobQualityIssue, JobQualityIssueAdmin)