from rest_framework import generics

from .models import JobQualityIssue
from .serializer import JobQualityIssueSerializer

# Create your views here.

class JobQualityIssueList(generics.ListCreateAPIView):
    queryset = JobQualityIssue.objects.all()
    serializer_class = JobQualityIssueSerializer

class JobQualityIssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobQualityIssue.objects.all()
    serializer_class = JobQualityIssueSerializer

