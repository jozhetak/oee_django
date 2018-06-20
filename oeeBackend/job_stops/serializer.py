from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import JobStop

class JobStopSerializer(ModelSerializer):
    job_order_data_id = StringRelatedField()
    stop_id = StringRelatedField()
    class Meta:
        model = JobStop
        fields = ('pk', 'job_order_data_id', 'stop_id', 'start_datetime', 'close_datetime',
                  'stop_time', 'stop_description')
        