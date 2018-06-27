from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import JobOrderData

class JobOrderDataSerializer(ModelSerializer):
    job_number_id = StringRelatedField()
    shift_id = StringRelatedField()
    class Meta:
        model = JobOrderData
        fields = ('pk', 'job_order', 'shift', 'job_partial_status', 'packaged_qty',
                  'retention_samples_qty', 'reworked_qty', 'q_issues_qty', 'rejected_qty',
                  'first_pass_qty', 'total_qty', 'job_process_time', 'planned_downtime',
                  'not_planned_downtime', 'workstation','job_performance_comments', 'job_quality_comments',
                  'start_datetime', 'close_datetime')

        