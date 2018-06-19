from rest_framework.serializers import ModelSerializer
from .models import Shift

class ShiftSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = ('pk', 'shift_name', 'start_time', 'end_time')