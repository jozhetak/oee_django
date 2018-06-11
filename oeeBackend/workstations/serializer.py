from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Workstation

class WorkstationSerializer(ModelSerializer):
    ws_plant = StringRelatedField()
    class Meta:
        model = Workstation
        fields = ('pk', 'ws_name', 'ws_type', 'ws_plant')
        # lookup_field = 'ws_plant'
        