from rest_framework import generics

from .models import JobStop
from .serializer import JobStopSerializer

# Create your views here.

class JobStopList(generics.ListCreateAPIView):
    queryset = JobStop.objects.all()
    serializer_class = JobStopSerializer

class JobStopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobStop.objects.all()
    serializer_class = JobStopSerializer

