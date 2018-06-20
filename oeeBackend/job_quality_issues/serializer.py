from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import JobQualityIssue

class JobQualityIssueSerializer(ModelSerializer):
    job_order_data_id = StringRelatedField()
    q_issue_id = StringRelatedField()
    class Meta:
        model = JobQualityIssue
        fields = ('pk', 'job_order_data_id', 'q_issue_id', 'q_issue_qty', 'reworked')
        # lookup_field = 'ws_plant'
        