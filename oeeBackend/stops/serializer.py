from rest_framework.serializers import ModelSerializer
from .models import Stop

class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = ('pk', 'stop_name', 'stop_type', 'stop_res_email')