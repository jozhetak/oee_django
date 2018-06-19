from rest_framework import generics

from .models import JobOrder
from .serializer import JobOrderSerializer

# Create your views here.

class JobOrderList(generics.ListCreateAPIView):
    queryset = JobOrder.objects.all()
    serializer_class = JobOrderSerializer

class JobOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOrder.objects.all()
    serializer_class = JobOrderSerializer

