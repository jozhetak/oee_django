from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Bom

class BomSerializer(ModelSerializer):
    item_id = StringRelatedField()
    workstation_id = StringRelatedField()
    class Meta:
        model = Bom
        fields = ('pk', 'item_id', 'workstation_id', 'production_rate')
        # lookup_field = 'ws_plant'
        