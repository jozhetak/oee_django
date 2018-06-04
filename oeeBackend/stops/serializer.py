from rest_framework.serializers import ModelSerializer
from .models import Stop

class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'