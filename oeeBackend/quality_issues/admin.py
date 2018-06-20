from django.contrib import admin
from .models import QualityIssue

# Register your models here.

class QualityIssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'q_issue', 'rework_rate', 'created_at', 'update_at')

admin.site.register(QualityIssue, QualityIssueAdmin)