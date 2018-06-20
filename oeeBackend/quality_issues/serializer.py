from rest_framework.serializers import ModelSerializer
from .models import QualityIssue

class QualityIssueSerializer(ModelSerializer):
    class Meta:
        model = QualityIssue
        fields = ('pk', 'q_issue', 'rework_rate')