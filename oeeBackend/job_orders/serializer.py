from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import JobOrder

class JobOrderSerializer(ModelSerializer):
    item_id = StringRelatedField()
    class Meta:
        model = JobOrder
        fields = ('pk', 'job_number', 'item_id', 'planned_qty', 'batch_number', 'due_date', 'job_status', 'start_datetime', 'close_datetime')

        