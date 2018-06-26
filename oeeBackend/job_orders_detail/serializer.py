from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import JobOrderDetail

class JobOrderDetailSerializer(ModelSerializer):
    job_order = StringRelatedField()
    item = StringRelatedField()
    workstation = StringRelatedField()
    class Meta:
        model = JobOrderDetail
        fields = ('pk', 'job_order_id', 'item', 'workstation', 'production_rate',)

        