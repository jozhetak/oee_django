from rest_framework import generics

from .models import JobOrderData
from .serializer import JobOrderDataSerializer

# Create your views here.

class JobOrderDataList(generics.ListCreateAPIView):
    queryset = JobOrderData.objects.all()
    serializer_class = JobOrderDataSerializer

class JobOrderDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOrderData.objects.all()
    serializer_class = JobOrderDataSerializer

