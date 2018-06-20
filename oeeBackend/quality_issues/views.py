from rest_framework import generics

from .models import QualityIssue
from .serializer import QualityIssueSerializer

# Create your views here.

class QualityIssueList(generics.ListCreateAPIView):
    queryset = QualityIssue.objects.all()
    serializer_class = QualityIssueSerializer

class QualityIssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QualityIssue.objects.all()
    serializer_class = QualityIssueSerializer
